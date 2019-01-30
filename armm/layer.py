"""
This module contains the attributes and methods of the `BaseLayer` 
class, as well as classes that derive from it. Each `BaseLayer` has some 
physical properties that we need to access (and possibly update) 
throughout our calculations.
"""

import numpy as np


class BaseLayer:
    """
    `BaseLayer` docstring.
    """
    def __init__(self, rind=1., thick=1., tand=0., desc='Basic layer'):
        self.rind = rind
        self.thick = thick # Arbitrary non-zero thickness to avoid div(0) errors
        self.tand = tand
        self.desc = desc

    def __repr__(self):
        return '{} (Basic layer)'.format(self.desc)

    def get_rind(self):
        return self.rind

    def get_thick(self):
        return self.thick

    def get_tand(self):
        return self.tand

    def get_desc(self):
        return self.desc


class Layer(BaseLayer):
    """
    `Layer` docstring.
    """
    def __init__(self, halperna=None, halpernb=None, **kwargs):
        super().__init__(**kwargs)
        self.desc = 'Layer'
        self.halperna = halperna
        self.halpernb = halpernb

class Source(BaseLayer):
    """
    `Source` docstring.
    """
    def __init__(self):
        super().__init__()
        self.thick = np.inf
        self.previous = _Void()
        self.desc = 'Source layer'

    def __repr__(self):
        return '{} (Source layer)'.format(self.desc)


class Terminator(BaseLayer):
    """
    `Terminator` docstring.

    Default case vac == True. `False` matches refractive index of previous
    layer, but attenuation is set to zero.
    """
    def __init__(self, vac=True):
        super().__init__()
        self.thick = np.inf
        self.next = _Void()
        self.desc = 'Terminator layer'
        self.vac = vac

    def __repr__(self):
        return '{} (Terminator layer)'.format(self.desc)


class _Void(BaseLayer):
    """     THE VOID     """
    def __init__(self):
        super().__init__()
        self.thick = np.inf
        self.desc = 'THE VOID'

    def __repr__(self):
        return 'There is nothing but {}'.format(self.desc)
