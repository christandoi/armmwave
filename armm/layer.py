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
    def __init__(self):
        self.rind = 1.
        self.thick = 1. # Arbitrary non-zero thickness to avoid div(0) errors
        self.tand = 0.
        self.desc = 'Basic layer'

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

class Source(BaseLayer):
    """
    `Source` docstring.
    """
    def __init__(self):
        super().__init__()
        self.thick = np.inf
        self.desc = 'Source layer'

    def __repr__(self):
        return '{} (Source layer)'.format(self.desc)

class Terminator(BaseLayer):
    """
    `Terminator` docstring.
    """
    def __init__(self):
        super().__init__()
        self.thick = np.inf
        self.desc = 'Terminating layer'

    def __repr__(self):
        return '{} (Terminator layer)'.format(self.desc)
