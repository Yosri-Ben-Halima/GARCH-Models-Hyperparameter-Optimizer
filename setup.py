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
