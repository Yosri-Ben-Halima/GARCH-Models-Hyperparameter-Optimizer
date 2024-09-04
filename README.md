   # GARCH Hyperparameter Optimization

   This project provides a GARCH hyperparameter grid search optimizer using Optuna.

   ## Installation

   Ensure you have the necessary packages installed. You can install them using pip:

   ```bash
   pip install -r requirements.txt
   ```

   ## Usage

   Import the `garch_parameter` function from the `garch_optimizer` module and use it to find the best GARCH model parameters:

   ```python
   from garch_optimizer.garch_optimizer import garch_parameter

   # Sample data for testing
   import pandas as pd
   import numpy as np
   np.random.seed(42)
   data = pd.Series(np.random.randn(100))

   best_params = garch_parameter(data, max_p=3, max_q=3, n_trials=200)
   print(best_params)
   ```

   ## Testing

   To run the tests, use the following command:

   ```bash
   python -m unittest discover
   ```

   ## License

   This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

   **`requirements.txt`**:
   ```
   optuna
   pandas
   numpy
   arch
   scikit-learn
   ```

   **`setup.py`**:
   ```python
   from setuptools import setup, find_packages

   setup(
       name='garch_optimizer',
       version='0.1',
       packages=find_packages(),
       install_requires=[
           'optuna',
           'pandas',
           'numpy',
           'arch',
           'scikit-learn',
       ],
       tests_require=[
           'unittest',
       ],
       description='GARCH Hyperparameter Grid Search Optimizer using Optuna',
       author='Your Name',
       author_email='your.email@example.com',
       url='https://github.com/yourusername/garch_optimizer',
   )
   ```

### Summary:
- **`garch_optimizer/`**: Contains the main code for the project.
- **`tests/`**: Contains unit tests for the project.
- **`README.md`**: Provides an overview and usage instructions.
-

 **`requirements.txt`**: Lists the project dependencies.
- **`setup.py`**: Allows installation of the package and its dependencies.

This setup follows PEP8 guidelines and provides a clean and organized project structure.
