"""
Contains tests for the `Model` class
"""

import unittest
import numpy as np
from armm import model

class ModelTest(unittest.TestCase):
    def setUp(self):
        self.model = model.Model()

    def test_set_freq_range_samples(self):
        low = 1.
        hi = 10.
        samp = 10
        sample_chkarr = np.linspace(low, hi, num=samp)
        sample_modarr = self.model.set_freq_range(low, hi, nsample=samp)
        self.assertTrue(np.array_equal(sample_chkarr, sample_modarr),
            msg='Frequency arrays are not equal.')

    def test_set_freq_range_single(self):
        low = 2.
        hi = 2.
        single_chkarr = np.array([2.])
        single_modarr = self.model.set_freq_range(low, hi)
        self.assertTrue(np.array_equal(single_chkarr, single_modarr),
            msg='Frequency arrays are not equal.')

    
