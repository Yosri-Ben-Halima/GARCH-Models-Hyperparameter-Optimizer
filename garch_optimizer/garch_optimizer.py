import optuna
import pandas as pd
import numpy as np
import logging
import time
from arch import arch_model
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.exceptions import ConvergenceWarning
from scipy.linalg import LinAlgError
import warnings

def garch_parameter(data, max_p, max_q, max_o=0, max_lag=0, vol=None, n_trials=200, x=None):
    """
    Perform hyperparameter optimization for GARCH model parameters using Optuna.

    Parameters
    -----------

    - data: array-like
        The input data for the GARCH model.
    - max_p: int 
        Maximum value for the GARCH(p, q, o) model's p parameter.
    - max_q: int 
        Maximum value for the GARCH(p, q, o) model's q parameter.
    - max_o: int, optional 
        Maximum value for the GARCH(p, q, o) model's o parameter. Defaults to 0.
    - max_lag: int, optional 
        Maximum value for the GARCH(p, q, o) model's lags parameter. Defaults to 0.
    - vol: str or list, optional
        Specification of the volatility model. If None, the model will be optimized among 'arch', 'garch', and 'egarch'. If it is a string, the provided volatility model will be used. If it is a list, the volatility model will be selected from the provided list of models. Defaults to None.
    - n_trials: int, optional 
        Number of optimization trials to perform. Defaults to 200.
    - x: array-like, optional
        The exogenous variable for the GARCH model. Defaults to None. Ignored if the model does not permit exogenous regressors.

    Returns
    -------

    - best_params: dict
        Best parameters found during the optimization.

    Raises
    ------

    - `LinAlgError`: If a LinAlgError occurs during the optimization process.
    - `RuntimeWarning`: If a RuntimeWarning occurs during the optimization process.
    - `ConvergenceWarning`: If a ConvergenceWarning occurs during the optimization process.
    """
    def objective(trial):
        """
        Objective function for Optuna optimization. 

        Parameters:
        - trial (optuna.Trial): Optuna trial object for suggesting parameter values.

        Returns:
        - float: Score for the trial. Returns np.inf if model fitting fails or p-values are not satisfactory.
        """
        try:
            p = trial.suggest_int('p', 1, max_p)
            q = trial.suggest_int('q', 1, max_q)
            o = trial.suggest_int('o', 0, max_o)
            lags = trial.suggest_int('lags', 0, max_lag)
            mean_model = trial.suggest_categorical('mean_model', ['constant', 'AR', 'zero'])
            
            if vol is None:
                vol_model = trial.suggest_categorical('vol_model', ['arch', 'garch', 'egarch'])
            elif isinstance(vol, list):
                vol_model = trial.suggest_categorical('vol_model', vol)
            else:
                vol_model = vol
            
            error_dist = trial.suggest_categorical('error_dist', ['normal', 'studentst', 'skewt', 'ged'])

            model = arch_model(data, mean=mean_model, vol=vol_model, p=p, q=q, o=o, lags=lags, rescale=True, x=x, dist=error_dist)
            model_fit = model.fit(disp='off')
            
            df = pd.DataFrame()
            df['Conditional Volatility'] = model_fit.conditional_volatility
            df['True Volatility'] = data.ewm(3).std()
            df.dropna(inplace=True)

            mape = mean_absolute_percentage_error(df['True Volatility'], df['Conditional Volatility'])

            score = model_fit.bic + (100 / model_fit.rsquared_adj if model_fit.rsquared_adj != 0 else np.inf) + 100 * mape

            pvals = [model_fit.pvalues[f'alpha[{p}]']]

            if vol_model != 'arch':
                pvals.append(model_fit.pvalues[f'beta[{q}]'])
            if o != 0 and vol_model != 'arch':
                pvals.append(model_fit.pvalues[f'gamma[{o}]'])

            if lags != 0 and mean_model == 'AR':
                pvals.append(model_fit.pvalues[f'{data.name}[{lags}]'])

            pvals = np.array(pvals)

            if not all(pvals < 0.05):
                score = np.inf

            return score

        except (LinAlgError, RuntimeWarning, ConvergenceWarning):
            return np.inf

    start_time = time.time()
    study = optuna.create_study(direction='minimize')

    # Suppress Optuna logs
    optuna_logger = logging.getLogger("optuna")
    optuna_logger.setLevel(logging.WARNING)
    
    study.optimize(objective, n_trials=n_trials, show_progress_bar=True, n_jobs=5)
    best_params = study.best_params

    if isinstance(vol, str):
        best_params['vol_model'] = vol

    best_score = study.best_value

    print("Best Parameters:", best_params)
    print("Best Score:", best_score)

    elapsed_time = time.time() - start_time
    print(f"Elapsed Time: {int(elapsed_time // 3600):02}:{int((elapsed_time % 3600) // 60):02}:{elapsed_time % 60:05.2f}")

    return best_params
