"""
Contains the methods and attributes of a `Model`, which is an assembly
of `Layer` objects.
"""

import numpy as np
import armm.layer
import armm.core

class Model:
    def __init__(self):
        self.struct = None
        self.low_freq = None
        self.high_freq = None
        self.freq_range = None
        self.pol = None
        self.incident_angle = None
        self.snell_angles = None
        self.rinds = None
        self.tands = None
        self.thicks = None
        self._sim_params = None

    def set_freq_range(self, low_freq, high_freq, nsample=1000):
        """
        Set the frequency range over which the model's response will be
        calculated.

        Note: Due to the vagaries of floating point arithmetic,
        specifying a `resolution` will yield an approximate resolution
        and not the exact one passed to the function. MIGHTFIX

        Arguments
        ---------

        Returns
        -------
        """
        if nsample <= 0:
            raise ValueError('nsample must be a positive number')
        self.low_freq = low_freq
        self.high_freq = high_freq
        if low_freq == high_freq:
            self.freq_range = np.array([low_freq])
        else:
            self.freq_range = np.linspace(low_freq, high_freq, num=nsample)
        return self.freq_range

    def set_angle_range(self, low_angle, high_angle, nsample=1000, resolution=0):
        """ Will implement once pi/2 is handled well """
        raise NotImplementedError('Coming soon! Maybe!')

    def set_up(self, layers, low_freq=500e6, high_freq=500e9, theta0=0., pol='s'):
        """
        Convenience function to get all the model bits and pieces in one
        place.

        Arguments
        ---------

        Returns
        -------
        """
        # Check that the first and last layers are infinite boundaries
        # and that there is at least one intervening material
        if len(layers) < 3:
            raise IndexError('Must pass a Source layer, at least one material '
                             'layer, and a Terminator layer.')
        if not isinstance(layers[0], armm.layer.Source):
            raise TypeError('The first layer must be a Source layer.')
        if not isinstance(layers[-1], armm.layer.Terminator):
            raise TypeError('The last layer must be a Terminator layer.')

        self.set_freq_range(low_freq=low_freq, high_freq=high_freq)
        self.incident_angle = theta0
        self.pol = pol
        self.struct = layers
        self.rinds = [l.rind for l in layers]
        self.tands = [l.tand for l in layers]
        self.thicks = [l.thick for l in layers]

        term_layer = self.struct[-1]
        last_material = self.struct[-2]
        if not term_layer.vac:
            term_layer.rind = last_material.rind

        # The model elements that we need for the calculations are slightly
        # different than those that the user may care about. For that reason,
        # we'll store the simulation parameters self._sim_params as a dict
        # and chalk it up as an implementation detail.
        self._sim_params = self._set_up_sim(self.rinds, self.tands, self.thicks,
                                            self.freq_range, self.incident_angle,
                                            self.pol)
        return

    def _set_up_sim(self, rinds, tands, thicks, freq_range, theta0, pol):
        """
        Ensure the user-supplied parameters are in a form that the core
        calculation functions expect.

        It is not recommended to call this function directly. Call
        `Model().set_up()` instead.

        Arguments
        ---------

        Returns
        -------
        simargs : dict
        """
        simargs = {'rind':rinds, 'tand':tands, 'thick':thicks, 'freq':freq_range}

        # Make sure we pass back important elements as numpy arrays instead
        # of the original lists
        for key, val in simargs.items():
            if not isinstance(val, np.ndarray):
                simargs[key] = np.asarray(val)
        simargs['theta0'] = theta0
        simargs['pol'] = pol
        return simargs

    def reset_model(self):
        """
        Reinitialize the `Model` with its default values: `None`.

        Arguments
        ---------
        None

        Returns
        -------
        None
        """
        for key, val in self.__dict__.items():
            self.__dict__[key] = None
        return
