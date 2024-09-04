import unittest
import pandas as pd
import numpy as np
import garch_optimizer.garch_optimizer as go

class TestGARCHParameter(unittest.TestCase):
    def setUp(self):
        # Sample data for testing
        np.random.seed(42)
        self.data = pd.Series(np.random.randn(100))
        
    def test_garch_parameter(self):
        # Test the function with default parameters
        best_params = go.garch_parameter(self.data, max_p=3, max_q=3, n_trials=10)
        self.assertIsInstance(best_params, dict)
        self.assertIn('p', best_params)
        self.assertIn('q', best_params)
        self.assertIn('o', best_params)
        self.assertIn('vol_model', best_params)
        self.assertIn('mean_model', best_params)

if __name__ == '__main__':
    unittest.main()
