"""
Contains tests for the core.py module.
"""

import unittest
import numpy as np
from armm import core

class CoreTest(unittest.TestCase):
    def test_rt_amp(self):
        pass

    def test_r_power(self):
        amps = [-2., 0., 2.]
        ans = [4., 0., 4.]
        vals = zip(amps, ans)
        for v in vals:
            with self.subTest(i=v):
                self.assertEqual(core.r_power(v[0]), v[1],
                    msg='Unexpected reflection power result.')

    def test_t_power_normal_incidence(self):
        amps = [-2., 0., 2.]
        ans = [8., 0., 8.]
        vals = zip(amps, ans)
        for v in vals:
            with self.subTest(i=v):
                self.assertEqual(core.t_power(v[0], 1., 2., 0., 0.), v[1],
                    msg='Unexpected transmission power result.')

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

    def test_t_interface_normal_incidence(self):
        params = [(0., 's'), (0., 'p')]
        ans = [2./3., 2./3.]
        vals = zip(params, ans)
        for v in vals:
            with self.subTest(i=v):
                self.assertEqual(
                    core.t_interface(1., 2., v[0][0], v[0][0], v[0][1]), v[1],
                    msg='Unexpected transmission at interface. Note: Trig operations'
                        ' in the vicinity of pi/2 are not currently handled well'
                        ' and result in strange behavior.')

    def test_wavenumber_normal_incidence(self):
        lossy = [True, False]
        ans = [2000*np.pi*np.sqrt(1 + 0.001j), 2000*np.pi]
        vals = zip(lossy, ans)
        f = 150e9
        n = 2.
        tand = 0.001
        theta = 0.
        for v in vals:
            with self.subTest(i=v):
                self.assertAlmostEqual(
                    core.wavenumber(f, n, tand, theta, v[0]), v[1],
                    msg='Unexpected transmission at interface. Note: Trig operations'
                        ' in the vicinity of pi/2 are not currently handled well'
                        ' and result in strange behavior.')

    @unittest.expectedFailure
    def test_t_power_orthogonal_incidence(self):
        amps = [-2., 0., 2.]
        for a in amps:
            with self.subTest(i=a):
                self.assertAlmostEqual(
                    core.t_power(a, 1., 2., np.pi/2., np.pi/2.), 0.,
                    places=18,
                    msg='Unexpected transmission power result. Note: Trig operations'
                        ' in the vicinity of pi/2 are not currently handled well'
                        ' and result in strange behavior.')

    @unittest.expectedFailure
    def test_r_interface_orthogonal_incidence(self):
        params = [(np.pi/2., 's'), (np.pi/2, 'p')]
        ans = [0, 0]
        vals = zip(params, ans)
        for v in vals:
            with self.subTest(i=v):
                self.assertEqual(
                    core.r_interface(1., 2., v[0][0], v[0][0], v[0][1]), v[1],
                    msg='Unexpected reflection at interface. Note: Trig operations'
                        ' in the vicinity of pi/2 are not currently handled well'
                        ' and result in strange behavior.')

    @unittest.expectedFailure
    def test_t_interface_orthogonal_incidence(self):
        params = [(np.pi/2., 's'), (np.pi/2., 'p')]
        ans = [0., 0.]
        vals = zip(params, ans)
        for v in vals:
            with self.subTest(i=v):
                self.assertEqual(
                    core.t_interface(1., 2., v[0][0], v[0][0], v[0][1]), v[1],
                    msg='Unexpected transmission at interface. Note: Trig operations'
                        ' in the vicinity of pi/2 are not currently handled well'
                        ' and result in strange behavior.')

    @unittest.expectedFailure
    def test_wavenumber_orthogonal_incidence(self):
        lossy = [True, False]
        ans = [0., 0.]
        vals = zip(lossy, ans)
        for v in vals:
            with self.subTest(i=v):
                self.assertEqual(
                    core.wavenumber(150e9, 2., 0.001, np.pi/2., v[0]), v[1],
                    msg='Unexpected transmission at interface. Note: Trig operations'
                        ' in the vicinity of pi/2 are not currently handled well'
                        ' and result in strange behavior.')

    def test_prop_wavenumber(self):
        ks = np.array([1., 1., 2., 2.])
        ds = np.array([np.inf, 2., 2., np.inf])
        ans = np.array([np.inf, 2., 4., np.inf])
        self.assertTrue(np.array_equal(core.prop_wavenumber(ks, ds), ans),
            msg='Unexpected propagation result')

    def test_make_2x2(self):
        nparr = np.array([[1., 2.], [3., 4.]])
        corearr = core.make_2x2(1., 2., 3., 4.)
        self.assertTrue(np.array_equal(nparr, corearr),
            msg='The output of core.make_2x2() is not the same as np.array()!')

    def test_refract_normal_incidence(self):
        ns = [1., 2., 4., 9., 4., 2., 1.]
        ans = [0.]*len(ns)
        output = core.refract(ns, 0)
        self.assertEqual(output, ans,
            msg='Unexepected output. Expected this:\n{}\n'
                'But got this:\n{}'.format(ans, output))

if __name__ == '__main__':
    unittest.main()
