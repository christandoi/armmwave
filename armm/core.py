"""
Contains the main transmission/reflection calculation bits

TODO
  * Fix the behavior of trig functions in the vicinity of pi/2
"""

import numpy as np
import scipy as sp

def rt_amp(index, delta, theta, pol):
    """
    Calculate the reflected and transmitted amplitudes through the
    system.

    Arguments
    ---------
    index : array
        An array of refractive indices, ordered from source layer to
        terminator layer.
    delta : array
        An array of wavevector offsets.
    theta : array
        An array of Snell angles in radians.
    pol : string
        The polarization of the source wave: 's' or 'p',
        or 'u'.

    Returns
    -------
    (r, t) : tuple
        A tuple where 'r' is the reflected amplitude, and 't' is the
        transmitted amplitude.
    """
    t_amp = np.zeros((len(self.structure), len(self.structure)),dtype=complex)
    r_amp = np.zeros((len(self.structure), len(self.structure)), dtype=complex)

    for i in range(len(self.structure)-1):
        t_amp[i, i+1] = t_interface(pol, index[i], index[i+1], theta[i], theta[i+1])
        r_amp[i, i+1] = r_interface(pol, index[i], index[i+1], theta[i], theta[i+1])
    
    m_matrix = np.zeros((len(self.structure), 2, 2), dtype=complex)
    m_r_amp = np.zeros((len(self.structure), 2, 2), dtype=complex)
    m_t_amp = np.zeros((len(self.structure), 2, 2), dtype=complex)
    # The following commented lines don't actually do anything...
    # They should be deleted once that is confirmed.
#    for i in range(1, len(self.structure)-1):
#        m_t_amp[i] = self._make_2x2(np.exp(-1j*deltas[i]), 0., 0.,
#                                    np.exp(1j*deltas[i]), dtype=complex)
#        m_r_amp[i] = self._make_2x2(1., r_amp[i, i+1], r_amp[i, i+1],
#                                    1., dtype=complex)
    for i in range(1, len(self.structure)-1):
        m_matrix[i] = (1/t_amp[i, i+1] * np.dot(
            make_2x2(np.exp(-1j*delta[i]), 0., 0., np.exp(1j*delta[i]), dtype=complex),
            make_2x2(1., r_amp[i, i+1], r_amp[i, i+1], 1., dtype=complex)))

    m_prime = make_2x2(1., 0., 0., 1., dtype=complex)
    for i in range(1, len(self.structure)-1):
        m_prime = np.dot(m_prime, m_matrix[i])

    m_prime = np.dot(make_2x2(1., r_amp[0, 1], r_amp[0, 1], 1., dtype=complex)/t_amp[0, 1], m_prime)
    trans_amp = 1/m_prime[0, 0]
    ref_amp = m_prime[0, 1]/m_prime[0, 0]
    return (ref_amp, trans_amp)

def r_power(r_amp):
    """
    Return fraction of reflected power.

    Arguments
    ---------
    r_amp : float
        The net reflection amplitude after calculating the transfer
        matrix.
    """
    return np.abs(r_amp)**2

def t_power(t_amp, index_i, index_f, theta_i, theta_f):
    """
    Return the fraction of transmitted power.

    Arguments
    ---------
    t_amp : float
        The net transmission amplitude after calculating the transfer 
        matrix.
    index_i : float
        The index of refraction of the source material.
    index_f : float
        The index of refraction of the terminating material.
    theta_i : float
        The angle of incidence (radians) at the initial interface.
    theta_f : float
        The angle of incidence (radians) at the final interface.
    """
    return np.abs(t_amp**2)*(index_f*np.cos(theta_f)/index_i*np.cos(theta_i))

def r_interface(index1, index2, theta1, theta2, pol):
    """
    Calculate the reflected amplitude at an interface.

    Arguments
    ---------
    index1 : float
        The index of refraction of the first material.
    index2 : float
        The index of refraction of the second material.
    theta1 : float
        The angle of incidence at interface 1, in radians
    theta2 : float
        The angle of incidence at interface 2, in radians
    pol : string
        The polarization of the source wave (either 's' or 'p').

    Returns
    -------
    reflected amplitude : float
        The amplitude of the reflected power
    """
    if pol == 's':
        s_numerator = (index1*np.cos(theta1) - index2*np.cos(theta2))
        s_denominator = (index1*np.cos(theta1) + index2*np.cos(theta2))
        return s_numerator/s_denominator
    elif pol == 'p':
        p_numerator = (index2*np.cos(theta1) - index1*np.cos(theta2))
        p_denominator = (index1*np.cos(theta2) + index2*np.cos(theta1))
        return p_numerator/p_denominator
    else:
        raise ValueError("Polarization must be 's' or 'p'")

def t_interface(index1, index2, theta1, theta2, pol):
    """
    Calculate the transmission amplitude at an interface.

    Arguments
    ---------
    index1 : float
        The index of refraction of the first material.
    index2 : float
        The index of refraction of the second material.
    theta1 : float
        The angle of incidence at interface 1, in radians
    theta2 : float
        The angle of incidence at interface 2, in radians
    pol : string
        The polarization of the source wave (either 's' or 'p').

    Returns
    -------
    transmitted_amplitude : float
        The amplitude of the transmitted power
    """
    if pol == 's':
        s_numerator = 2*index1*np.cos(theta1)
        s_denominator = (index1*np.cos(theta1) + index2*np.cos(theta2))
        return s_numerator/s_denominator
    elif pol == 'p':
        p_numerator = 2*index1*np.cos(theta1)
        p_denominator = (index1*np.cos(theta2) + index2*np.cos(theta1))
        return p_numerator/p_denominator
    else:
        raise ValueError("Polarization must be 's' or 'p'")

def wavenumber(freq, index, tand, theta, lossy=True):
    """
    Calculate the wavenumbers.

    Arguments
    ---------
    freq : float
        The frequency at which to calculate the wavevector, k
    tand : array
        An array of loss tangents, ordered from source to terminating
    index : array
        An array of refractive indices, ordered from source to
        terminating layer
        layer
    theta : array
        An array of Snell angles (radians)
    lossy : bool, optional
        If `True` the wavevector will be found for a lossy material.
        If `False` the wavevector will be found for lossless material.
        Default is `True`.

    Returns
    -------
    k : array
        The complex wavenumber, k
    """
    if lossy:
#        k = (2*np.pi*index*freq*np.cos(theta)/3e8 * (1 + 0.5j*tand))
        k = (2*np.pi*index*freq*np.cos(theta)/3e8 * np.sqrt((1 + 1j*tand)))

#        c = 3e8
#        a = 0.0926
#        b = 0.840
#        alpha = a*(freq/3e10)**b
#        kap = (alpha*3e8)/(2*100*np.pi*freq*index)
#        pre = 2*np.pi/c
#        real = index**2 - kap**2
#        imag = 2*index*kap
#        tand = kap
#        k = (2*np.pi*index*freq*np.cos(theta)/3e8 * (1+0.5j*tand))
#        k = ((2*np.pi*index*np.cos(theta)*freq/3e10 + 
#              1j*(0.0926*((freq/3e10)**0.840))/2))*100
    else:
        k = 2*np.pi*index*freq/3e8
    return k

def make_2x2(a11, a12, a21, a22, dtype=float):
    """
    Return a 2x2 array quickly.

    Thanks to Steve Byrnes for this one.

    Arguments
    ---------
    a11 : float
        Array element [0, 0].
    a12 : float
        Array element [0, 1].
    a21 : float
        Array element [1, 0].
    a22 : float
        Array element [1, 1].
    dtype : dtype, optional
        The datatype of the array. Defaults to float.
    """
    array = np.empty((2, 2), dtype=dtype)
    array[0, 0] = a11
    array[0, 1] = a12
    array[1, 0] = a21
    array[1, 1] = a22
    return array

def prop_wavenumber(k, d):
    """
    Calculate the wavenumber offset, delta.

    Arguments
    ---------
    k : array
        The wavevector
    d : array
        An array of distances (thicknesses), ordered from source to
        terminating layer

    Returns
    -------
    delta : array
        The phase difference
    """
    # Turn off 'invalid multiplication' error;
    # It's just the 'inf' boundaries.
    olderr = sp.seterr(invalid='ignore')
    delta = k*d
    # Now turn the error back on
    sp.seterr(**olderr)
    return delta
