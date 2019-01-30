"""
Contains tests for the `Model` class
"""

import unittest
import numpy as np
from armm import model
from armm import layer

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

    def test_set_up_errors(self):
        # layers1 should throw an IndexError; layers2 should throw a
        # TypeError; layers3 should throw a TypeError
        layers1 = [[layer.BaseLayer()]]
        layers2 = [[layer.BaseLayer(), layer.BaseLayer(), layer.Terminator()]]
        layers3 = [[layer.Source(), layer.BaseLayer(), layer.BaseLayer()]]
        vals = layers1 + layers2 + layers3
        errs = (IndexError, TypeError)
        for v in vals:
            with self.subTest(i=v):
                self.assertRaises(errs, self.model.set_up, v[0])

    def test_set_up_match_term_rind(self):
        last_rind = -99.0
        layers = [layer.Source(), layer.BaseLayer(),
                  layer.BaseLayer(rind=last_rind), layer.Terminator()]
        vac = [False, True]
        ans = [last_rind, 1.]
        vals = zip(vac, ans)
        for v in vals:
            with self.subTest(i=v):
                layers[-1] = layer.Terminator(vac=v[0])
                self.model.set_up(layers)
#                print(self.model.struct)
                terminator = self.model.struct[-1]
                self.assertEqual(terminator.rind, v[1],
                    msg='Unexpected Terminator refractive index. '
                        'Got: {}'.format(terminator.rind))
