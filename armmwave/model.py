"""
Contains the methods and attributes of a `Model`, which is an assembly
of `Layer` objects.
"""
import sys
import numpy as np
import armmwave.layer
import armmwave.core

class Model:
    """
    The `Model` class is the framework used to assemble the simulation
    `Layer`s. It serves as an entry-point to the main calculation.

    Parameters
    ----------
    None

    Attributes
    ----------
    struct : list
        A collection of `Layer` objects as assembled by the `set_up()`
        class method.
    low_freq : float
        The low-frequency (Hz) bound for the calculation. May be set directly or
        through the `set_freq_range()` class method. Defaults to 500 MHz if
        not set before `run()` is called.
    high_freq : float
        The high-frequency (Hz) bound for the calculation. May be set directly or
        through the `set_freq_range()` class method. Defaults to 500 GHz if
        not set before `run()` is called.
    freq_range : list or numpy array
        The frequencies (Hz) at which to run the calculation. Defaults to
        [500e6, 500e9] with 1000 evenly-spaced samples if not set before
        `run()` is called.
    pol : string
        The target polarization, either 's' or 'p'. Defaults to 's' if not
        set before `run()` is called.
    incident_angle : float
        The initial angle (in radians; with respect to normal) at which the
        wave should strike the model. Defaults to 0 if not set before `run()`
        is called.
    rinds : list or numpy array
        A collection of refractive indices for each `Layer` in the model,
        ordered from `Source` to `Terminator`.
    tands : list or numpy array
        A collection of loss tangents for each `Layer` in the model,
        ordered from `Source` to `Terminator`.
    halpern_layers : dict
        A dictionary, keyed by `Layer` position (specifically, the index into
        `tands`) containing Halpern 'a' and 'b' coefficients, if they exist.
        These coefficients are used to calculate a frequency-dependent loss
        term, and override the loss tangent for the corresponding layer.
    thicks : list or numpy array
        A collection of thicknesses (in meters) for each `Layer` in the model,
        ordered from `Source` to `Terminator`.

    Methods
    -------
    reset_model
    run
    save
    set_freq_range
    set_angle_range
    set_up
    """

    def __init__(self):
        self.struct = None
        self.low_freq = None
        self.high_freq = None
        self.freq_range = None
        self.pol = None
        self.incident_angle = None
        self.rinds = None
        self.tands = None
        self.halpern_layers = None
        self.thicks = None
        self._sim_params = None
        self._sim_results = None

    def set_freq_range(self, freq1, freq2, nsample=1000):
        """
        Set `self.freq_range`, the frequency range over which the model's
        response will be calculated.

        Parameters
        ----------
        freq1 : float
            Typically, the lower frequency bound (in Hz). However, you
            may run the calculation from high to low frequency if you wish.
        freq2 : float
            Typically, the upper frequency bound (in Hz). However, you
            may run the calculation from high to low frequency if you wish.
        nsample : int, optional
            The number of evenly-spaced samples between `freq1` and `freq2`.
            Default is 1000.

        Returns
        -------
        freq_range : numpy array
        """
        if nsample <= 0:
            raise ValueError('nsample must be a positive number')
        self.low_freq = min(freq1, freq2)
        self.high_freq = max(freq1, freq2)
        if freq1 == freq2:
            self.freq_range = np.array([freq1])
        else:
            self.freq_range = np.linspace(freq1, freq2, num=nsample)
        return self.freq_range

    def set_angle_range(self, angle1, angle2, nsample=50):
        """ Will implement once pi/2 is handled well """
        raise NotImplementedError('Coming soon! Maybe!')

    def set_up(self, layers, low_freq=500e6, high_freq=500e9, theta0=0., pol='s'):
        """
        Convenience function to get all the model bits and pieces in one
        place. Call this before calling `run()`.

        Parameters
        ----------
        layers : list
            A list containing `Layer` objects ordered from `Source` to
            `Terminator`. Note that the `Source` and `Terminator` layers
            should be the first and last entries of the list, respectively.
        low_freq : float, optional
            The lower frequency bound (in Hz). Default is 500e6 (500 MHz).
        high_freq : float, optional
            The upper frequency bound (in Hz). Default is 500e9 (500 GHz).
        theta0 : float, optional
            The initial angle (radians; with respect to normal) at which the
            wave should strike the model. Default is 0.
        pol : string, optional
            The target polarization for the calculation. Must be either 's',
            or 'p'. Default is 's'.
        """
        # Check that the first and last layers are infinite boundaries
        # and that there is at least one intervening material
        if len(layers) < 3:
            raise IndexError('Must pass a Source layer, at least one material '
                             'layer, and a Terminator layer.')
        if not isinstance(layers[0], armmwave.layer.Source):
            raise TypeError('The first layer must be a Source layer.')
        if not isinstance(layers[-1], armmwave.layer.Terminator):
            raise TypeError('The last layer must be a Terminator layer.')

        self.struct = layers
        term_layer = self.struct[-1]
        last_material = self.struct[-2]
        # It could be that we want to use a terminating layer with a refractive
        # index != 1, so we'll check for that here. If the user has set a n
        # to be something other than 1, then we don't really care what they
        # set 'vac' to be, so we short circuit that logic.
        if term_layer.rind == 1.0:
            if not term_layer.vac:
                term_layer.rind = last_material.rind
        # We need to check whether any of the layers will use a frequency-
        # dependent loss tangent based on Halpern's 'a' and 'b' coefficients.
        # If so, we need to pass the position of that layer to the core code
        # so it knows which layers have a static loss tangent. We will also
        # pass the 'a', 'b', and 'n' of the layer so that everything we need
        # to calculate the loss tangent is in one place. It's easiest to do
        # this with a dictionary that is keyed by the list index of the layer(s)
        # in question
        self.halpern_layers = {}
        for index, l in enumerate(self.struct):
            if l.desc != 'Source layer' and l.desc != 'Terminator layer':
                if isinstance(l.halperna, float) and isinstance(l.halpernb, float):
                    self.halpern_layers[index] = {'a':l.halperna, 'b':l.halpernb,
                                                  'n':l.rind}

        self.rinds = [l.rind for l in self.struct]
        self.tands = [l.tand for l in self.struct]
        self.thicks = [l.thick for l in self.struct]
        if self.freq_range is None:
            self.set_freq_range(freq1=low_freq, freq2=high_freq)
        if np.isclose(theta0, np.pi/2):
            raise ValueError('Incident angle is too close to pi/2. '\
                             'Maximum allowed angle is '\
                             '89.999 degrees ~= 1.5707788735023767 radians.')
        self.incident_angle = theta0
        self.pol = pol

        # The model elements that we need for the calculations are slightly
        # different than those that the user may care about. For that reason,
        # we'll store the simulation parameters self._sim_params as a dict
        # and chalk it up as an implementation detail.
        self._sim_params = self._set_up_sim(self.rinds, self.tands, self.thicks,
                                            self.freq_range, self.incident_angle,
                                            self.pol, self.halpern_layers)
        return

    def _set_up_sim(self, rinds, tands, thicks, freq_range, theta0, pol,
                    halpern_layers):
        """
        Ensure the user-supplied parameters are in a form that the core
        calculation functions expect.

        It is not recommended to call this function directly. Call
        `Model().set_up()` instead.

        Parameters
        ----------
        rinds : list or numpy array
        tands : list or numpy array
        thicks : list or numpy array
        freq_range : list or numpy array
        theta0 : float
        pol : string
        halpern_layers : dict

        Returns
        -------
        simargs : dict
        """
        sim_args = {'rind':rinds, 'tand':tands, 'thick':thicks, 'freq':freq_range}

        # Make sure we pass back important elements as numpy arrays instead
        # of the original lists
        for key, val in sim_args.items():
            if not isinstance(val, np.ndarray):
                sim_args[key] = np.asarray(val)
        sim_args['theta0'] = theta0
        sim_args['pol'] = pol
        sim_args['halpern_layers'] = halpern_layers
        return sim_args

    def reset_model(self):
        """Reinitialize the `Model` with its default attribute values: `None`."""
        for key, val in self.__dict__.items():
            self.__dict__[key] = None
        return

    def run(self):
        """
        Calculate transmittance and reflectance for the given model.

        This function is the primary entry-point to the main calculations.

        Returns
        -------
        results : dict
            A dictionary with three keys:
             * `frequency` : numpy array of frequencies corresponding
               to 'T' and 'R'
             * `transmittance` : numpy array of transmittances (T) for each
               frequency
             * `reflectance` : numpy array of reflectances (R) for each
               frequency
        """
        try:
            assert bool(self._sim_params)
        except AssertionError:
            raise KeyError('Did not find calculation-ready parameters. '
                           'Must call `set_up()` before calling `run()`')
        results = armmwave.core.main(self._sim_params)
        self._sim_results = results
        return results

    def save(self, dest):
        """
        Write transmittance and reflectance calculation results to a file,
        including a header describing the simulation parameters.
        """
        fs = self._sim_results['frequency']
        rs = self._sim_results['reflectance']
        ts = self._sim_results['transmittance']

        header = [
            'Structure: {}'.format(self.struct),
            'Frequency lower bound (Hz): {}'.format(self.low_freq),
            'Frequency upper bound (Hz): {}'.format(self.high_freq),
            'Incident angle (rad): {}'.format(self.incident_angle),
            'Polarization: {}'.format(self.pol),
            'Refractive indices: {}'.format(self.rinds),
            'Loss tangents: {}'.format(self.tands),
            'Thicknesses (m): {}'.format(self.thicks),
            '\n',
            'Frequency\t\t\tTransmittance\t\t\tReflectance',]

        np.savetxt(dest, np.c_[fs, ts, rs], delimiter='\t',
                    header='\n'.join(header))
        return
