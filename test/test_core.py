"""
Contains tests for the core.py module.
"""

import unittest
import numpy as np
from armm import core

class CoreTest(unittest.TestCase):
    def setUp(self):
        # We need to create a set of default values that we can use as
        # a baseline.
        self.index = 1.
        self.thick = 1.
        self.tand = 0.
        self.freq = 150e9 # frequency in Hz

    def test_rt_amp(self):
        pass

    def test_r_power(self):
        amps = [-2., 0., 2.]
        ans = [4., 0., 4.]
        vals = zip(amps, ans)
        for v in vals:
            with self.subTest(i=v):
                self.assertEqual(core.r_power(v[0]), v[1],
                    'Unexpected reflection power result.')

    def test_t_power_normal_incidence(self):
        amps = [-2., 0., 2.]
        ans = [8., 0., 8.]
        vals = zip(amps, ans)
        for v in vals:
            with self.subTest(i=v):
                self.assertEqual(core.t_power(v[0], 1., 2., 0., 0.), v[1],
                    'Unexpected transmission power result.')

#    def test_t_power_normal_orthogonal(self):
#        amps = [-2., 0., 2.]
#        for a in amps:
#            with self.subTest(i=a):
#                self.assertAlmostEqual(
#                    core.t_power(a, 1., 2., np.pi/2., np.pi/2.), 0.,
#                    places=18,
#                    msg='Unexpected transmission power result.')
    
    def test_r_interface_normal_incidence(self):
        params = [(0., 's'), (0., 'p')]
        ans = [-1./3., 1./3.]
        vals = zip(params, ans)
        for v in vals:
            with self.subTest(i=v):
                self.assertEqual(
                    core.r_interface(1., 2., v[0][0], v[0][0], v[0][1]), v[1],
                    msg='Unexpected reflection at interface. Note: Trig operations'
                        ' in the vicinity of pi/2 are not currently handled well'
                        ' and result in strange behavior.')

#    def test_r_interface_orthogonal_incidence(self):
#        params = [(np.pi/2., 's'), (np.pi/2, 'p')]
#        ans = [0, 0]
#        vals = zip(params, ans)
#        for v in vals:
#            with self.subTest(i=v):
#                self.assertEqual(
#                    core.r_interface(1., 2., v[0][0], v[0][0], v[0][1]), v[1],
#                    msg='Unexpected reflection at interface. Note: Trig operations'
#                        ' in the vicinity of pi/2 are not currently handled well'
#                        ' and result in strange behavior.')


    def test_t_interface(self):
        pass

    def test_wavenumber(self):
        pass

    def test_make_2x2(self):
        nparr = np.array([[1., 2.], [3., 4.]])
        corearr = core.make_2x2(1., 2., 3., 4.)
        self.assertTrue(np.array_equal(nparr.all(), corearr.all()),
            'The output of core.make_2x2() is not the same as np.array()!')

    def test_prop_wavenumber(self):
        pass

if __name__ == '__main__':
    unittest.main()
