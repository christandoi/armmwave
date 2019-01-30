"""
This set of tests evaluates the `BaseLayer` class and those classes that
inherit from it.
"""

import unittest
import numpy as np
from armm import layer

class BaseLayerTest(unittest.TestCase):
    def setUp(self):
        self.base_layer = layer.BaseLayer()

    def test_default_index(self):
        self.assertEqual(self.base_layer.get_rind(), 1.,
                         'Default rind (refractive index) is not equal to 1.')

    def test_default_thick(self):
        self.assertEqual(self.base_layer.get_thick(), 1.,
                         'Default thick (thickness) is not equal to 1.')

    def test_default_tand(self):
        self.assertEqual(self.base_layer.get_tand(), 0.,
                         'Default tand (loss tangent) is not equal to 0.')

    def test_default_desc(self):
        self.assertEqual(self.base_layer.get_desc(), 'Basic layer',
                         'Default desc (description) is not "Basic layer".')

    def test_set_index(self):
        self.base_layer.rind = 10.
        self.assertEqual(self.base_layer.get_rind(), 10.,
                         'rind (refractive index) is not equal to 10.')

    def test_set_thick(self):
        self.base_layer.thick = 10.
        self.assertEqual(self.base_layer.get_thick(), 10.,
                         'thick (thickness) is not equal to 10.')

    def test_set_tand(self):
        self.base_layer.tand = 10.
        self.assertEqual(self.base_layer.get_tand(), 10.,
                         'tand (loss tangent) is not equal to 10.')

    def test_set_desc(self):
        self.base_layer.desc = 'foo'
        self.assertEqual(self.base_layer.get_desc(), 'foo',
                         'desc (description) is not "foo".')

class SourceLayerTest(unittest.TestCase):
    def setUp(self):
        self.source_layer = layer.Source()

    def test_default_index(self):
        self.assertEqual(self.source_layer.get_rind(), 1.,
                         'Default rind (refractive index) is not equal to 1.')

    def test_default_thick(self):
        self.assertEqual(self.source_layer.get_thick(), np.inf,
                         'Default thick (thickness) is not infinite.')

    def test_default_tand(self):
        self.assertEqual(self.source_layer.get_tand(), 0.,
                         'Default tand (loss tangent) is not equal to 0.')

    def test_default_desc(self):
        self.assertEqual(self.source_layer.get_desc(), 'Source layer',
                         'Default desc (description) is not "Source layer".')

    def test_set_index(self):
        self.source_layer.rind = 10.
        self.assertEqual(self.source_layer.get_rind(), 10.,
                         'rind (refractive index) is not equal to 10.')

    def test_set_thick(self):
        self.source_layer.thick = 10.
        self.assertEqual(self.source_layer.get_thick(), 10.,
                         'thick (thickness) is not equal to 10.')

    def test_set_tand(self):
        self.source_layer.tand = 10.
        self.assertEqual(self.source_layer.get_tand(), 10.,
                         'tand (loss tangent) is not equal to 10.')

    def test_set_desc(self):
        self.source_layer.desc = 'foo'
        self.assertEqual(self.source_layer.get_desc(), 'foo',
                         'desc (description) is not "foo".')

class TerminatorLayerTest(unittest.TestCase):
    def setUp(self):
        self.terminator_layer = layer.Terminator()

    def test_default_index(self):
        self.assertEqual(self.terminator_layer.get_rind(), 1.,
                         'Default rind (refractive index) is not equal to 1.')

    def test_default_thick(self):
        self.assertEqual(self.terminator_layer.get_thick(), np.inf,
                         'Default thick (thickness) is not infinte')

    def test_default_tand(self):
        self.assertEqual(self.terminator_layer.get_tand(), 0.,
                         'Default tand (loss tangent) is not equal to 0.')

    def test_default_desc(self):
        self.assertEqual(self.terminator_layer.get_desc(), 'Terminating layer',
                         'Default desc (description) is not "Terminating layer".')

    def test_set_index(self):
        self.terminator_layer.rind = 10.
        self.assertEqual(self.terminator_layer.get_rind(), 10.,
                         'rind (refractive index) is not equal to 10.')

    def test_set_thick(self):
        self.terminator_layer.thick = 10.
        self.assertEqual(self.terminator_layer.get_thick(), 10.,
                         'thick (thickness) is not equal to 10.')

    def test_set_tand(self):
        self.terminator_layer.tand = 10.
        self.assertEqual(self.terminator_layer.get_tand(), 10.,
                         'tand (loss tangent) is not equal to 10.')

    def test_set_desc(self):
        self.terminator_layer.desc = 'foo'
        self.assertEqual(self.terminator_layer.get_desc(), 'foo',
                         'desc (description) is not "foo".')

if __name__ == '__main__':
    unittest.main()
