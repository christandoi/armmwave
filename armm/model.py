"""
Contains the methods and attributes of a `Model`, which is an assembly
of `Layer` objects.
"""

import numpy as np
import armm.layer

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

    def freq_range(self, low_freq, high_freq, nsamples=1000, resolution=0):
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
        endpoint = True
        if resolution > 0:
            nsamples = round((high_freq - low_freq)/resolution)
            endpoint = False

        self.low_freq = low_freq
        self.high_freq = high_freq
        self.freq_range = np.linspace(low_freq, high_freq, num=nsamples,
                                       endpoint=endpoint)
        return

#    def angle_range(self, low_angle, high_angle, nsamples=1000, resolution=0):
#        """ Will implement once pi/2 is handled well """
#        raise NotImplemented


class Structure:
    def __init__(self):
        self.order = []

    def assemble(self, layers):
        """
        Layers should be a list of layer objects
        """
        pass
