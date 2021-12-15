import numpy as np
import pywt

def wEntropy(time_series, base = 'db1', level = 7):  
    """ Calculate the Wavelet entropy
    Parameters
    ----------
    time_series :   Time series                                     (np.array)
    base        :   Wavelet Base to calculate wavelet coefficients  (str)
    level       :   Level wavelet decomposition                     (int)
    
    Returns
    -------
    we          :   Wavelet Entropy                                 (float)
    """
    
    data = pywt.wavedec(time_series, base, level = level)

    Etot=0
    Ei = np.ones(level + 1) * 0

    for i, d in enumerate(data):
        Ei[i] = np.sum(d**2)
        Etot += Ei[i]
        Pi = Ei/Etot

    we = -np.sum(Pi*np.log(Pi))
    we = we / np.log(np.math.factorial(level))
    
    return we


