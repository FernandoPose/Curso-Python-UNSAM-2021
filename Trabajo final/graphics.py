import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np

def graficar_canal(channel,n_canal,Fs=256):
    x= np.linspace(0, len(channel)/Fs,len(channel))

    figure(figsize=(14,4), dpi=80)

    plt.plot(x,channel, color='blue')
    plt.title('Señal correspondiente al canal '+str(n_canal))
    plt.xlabel('seg [s]')
    plt.ylabel('EEG [uV]')
    plt.show()


def graficar_entropy(signal, wEntropy):
    """ Calculate the permutation entropy
    Parameters
    ----------
    time_series     :   Time series column          (np.array)
    wEntropy        :   Wavelet entropy serie       (np.array)   
    """

    fig, axs = plt.subplots(2)
    fig.suptitle('Results')

    axs[0].plot(signal)
    axs[0].set_ylabel('EEG [uV]')

    axs[1].plot(wEntropy)
    axs[1].set_ylabel('Wavelet Entropy')
    axs[1].set_xlabel('Windows')
    plt.show()