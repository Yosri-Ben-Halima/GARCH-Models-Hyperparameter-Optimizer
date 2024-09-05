# GARCH Hyperparameter Optimization

This project provides a GARCH hyperparameter grid search optimizer using Optuna.

## Project Structure

```bash
GARCH-Models-Hyperparameter-Optimizer/
│
├── garch_optimizer/
│   ├── __init__.py
│   └── garch_optimizer.py
│
├── tests/
│   ├── __init__.py
│   └── test_garch_optimizer.py
│
├── Analysis.ipynb  # Jupyter notebook
│
├── setup.py
├── requirements.txt
├── LICENSE
└── README.md

```
- **`garch_optimizer/`**: Contains the main code for GARCH hyperparameter optimization. The core functionality is implemented in `garch_optimizer.py`.
- **`tests/`**: Includes unit tests to verify the correctness of the optimizer. The `test_garch_optimizer.py` file contains test cases for the GARCH optimizer.
- **`Analysis.ipynb`**: A Jupyter notebook demonstrating how the GARCH optimizer works, with examples and visualizations.
- **`setup.py`**: Handles the packaging and installation of the project, specifying dependencies and metadata.
- **`requirements.txt`**: Lists the required Python packages needed to run the project.
- **`LICENSE`**: The license under which the project is released.
- **`README.md`**: The main documentation file providing an overview of the project, installation instructions, and usage examples.

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

best_params = garch_parameter(
        data=data, 
        max_p=3, 
        max_q=3, 
        n_trials=200
    )

print(best_params)
```

## Testing

To run the tests, use the following command:

```bash
python -m unittest discover
```

## Contributing

Feel free to submit issues or pull requests to enhance the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Thank you for visiting my GitHub profile! Feel free to reach out if you have any questions or opportunities to collaborate. Let's connect and explore new possibilities together!

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Yosri%20Ben%20Halima-blue)](https://www.linkedin.com/in/yosri-ben-halima-3553a9221/)
[![Twitter](https://img.shields.io/badge/Facebook-@Yosry%20Ben%20Hlima-navy)](https://www.facebook.com/NottherealYxsry)
[![Instagram](https://img.shields.io/badge/Instagram-@yosrybh-orange)](https://www.instagram.com/yosrybh/)
[![Email](https://img.shields.io/badge/Email-yosri.benhalima@ept.ucar.tn-white)](yosri.benhalima@ept.ucar.tn)

