"""
This module contains the attributes and methods of the ``BaseLayer``
class, and classes that inherit from it. Each ``BaseLayer`` has
some physical properties that we need to access (and possibly update)
throughout our calculations.
"""

import numpy as np


class BaseLayer:
    """The ``BaseLayer`` class is the parent from which all other classes
    derive. Its purpose is to establish the bare-minimum attributes
    needed for a given layer.

    Attributes
    ----------
    rind : float
        The refractive index of the layer. Default is 1.
    thick : float
        The thickness of the layer (in meters). Default is 1.
    tand : float
        The loss tangent of the layer. Default is 0---i.e., a lossless
        material.
    desc : str
        A descriptive string for the layer. For example, the name of the
        material. Default is 'Basic layer'.
    """
    def __init__(self, rind=1., thick=1., tand=0., desc='Basic layer'):
        self.rind = rind
        self.thick = thick # Arbitrary non-zero thickness to avoid div(0) errors
        self.tand = tand
        self.desc = desc

    def __repr__(self):
        return '{} (Basic layer)'.format(self.desc)

    def get_rind(self):
        """Return the layer refractive index."""
        return self.rind

    def get_thick(self):
        """Return the layer thickness."""
        return self.thick

    def get_tand(self):
        """Return the layer loss tangent."""
        return self.tand

    def get_desc(self):
        """Return the layer description."""
        return self.desc


class Layer(BaseLayer):
    """The ``Layer`` class is the primary class for model creation. Inherits
    from ``BaseLayer``.

    Parameters
    ----------
    rind : float, optional
        The refractive index of the layer. Default is 1.
    thick : float, optional
        The thickness of the layer (in meters). Default is 1.
    tand : float, optional
        The loss tangent of the layer. Default is 0---i.e., a lossless
        material.
    halperna : float, optional
        The Halpern `a` coefficient, used to caclulate a frequency-dependent
        loss tangent term. Default is `None`, which corresponds to a constant
        loss term.
    halpernb : float, optional
        The Halpern `b` coefficient, used to caclulate a frequency-dependent
        loss tangent term. Default is `None`, which corresponds to a constant
        loss term.
    desc : str, optional
        A descriptive string for the layer. For example, the name of the
        material. Default is 'Basic layer'
    """
    def __init__(self, halperna=None, halpernb=None, **kwargs):
        super().__init__(**kwargs)
        self.halperna = halperna
        self.halpernb = halpernb

    def __repr__(self):
        return '{} (Sim layer)'.format(self.desc)


class Source(BaseLayer):
    """The ``Source`` is required to be the first layer in the stack. Inherits
    from ``BaseLayer``.

    The source may have any refractive index or loss tangent, but it is
    required to have infinite thickness.

    NOTE: While it is possible to set the loss tangent of the layer to a
    non-zero value, it is not recommended. The case of an absorbing
    initial medium is not implemented yet.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.thick = np.inf
        self.previous = _Void()
        self.desc = 'Source layer'

    def __repr__(self):
        return '{} (Source layer)'.format(self.desc)


class Terminator(BaseLayer):
    """The ``Terminator`` is required to be the last layer in the stack.
    Inherits from ``BaseLayer``.

    The ``Terminator`` may have any refractive index or loss tangent, but
    it must have infinite thickness. As a convenience, the Terminator layer
    may be instantiated with the `vac` flag, where the default is `vac ==
    True`. `True` sets the refractive index of the ``Terminator`` to 1, and its
    attenuation to 0. `False` matches refractive index of previous
    layer, again setting the ``Terminator`` attenuation to zero.
    """
    def __init__(self, vac=True, **kwargs):
        super().__init__(**kwargs)
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

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.thick == other.thick and self.desc == 'THE VOID'
        return False

    def __repr__(self):
        return 'There is nothing but {}'.format(self.desc)
