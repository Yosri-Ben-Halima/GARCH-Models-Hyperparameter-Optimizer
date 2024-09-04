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
    author='Yosri Ben Halima',
    author_email='yosri.benhalima@ept.ucar.tn',
    url='https://github.com/Yosri-Ben-Halima/GARCH-Models-Hyperparameter-Optimize',
)
