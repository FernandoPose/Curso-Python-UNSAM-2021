import numpy as np
import scipy.io as sio     
import entropies as ent
import graphics as aux
import sys
   
#! python3 tp_final.py 'eeg_epilepsia.mat' 3
#! python3 tp_final.py

def main(archivo, n_canal):

    # Leo los datos
    data= sio.loadmat(archivo)

    #Me quedo con una matriz de 23 x 7168 = channels x samples
    data_matrix=data.get('data')[0][0][0]
    # print('Tamaño: ',data_matrix.shape)
    
    max_canales, _ = data_matrix.shape 
    
    if n_canal == None:
        flag = 1
        while flag == 1:
            n_canal = int(input(f"Introducir un canal entre 1 y {max_canales}: "))
            if n_canal <= max_canales:
                flag = 0
            else:
                print(f'Valor de canal incorrecto. (Cantidad de canales disponibles: {max_canales}. Seleccione -1 para salir.')
                
    try: 
        
        if n_canal != -1:
            channel=data_matrix[n_canal]

            # Ventanas de 100 muestras y 100 solapadas
            Fs = 256

            # Grafico señal
            aux.graficar_canal(channel,n_canal)

            # Set auxiliary segmentation signals
            nWindow 	= 4 * Fs # 4*256 samples (4 Fs)
            overlap 	= 1 * Fs # 256 samples (1 Fs)
            noverlap 	= nWindow - overlap

            # Calculo wavelet entropy
            base    = 'db1'  # Base de la wavelet daubechies
            level   = 4      # Nivel de descomposición                         

            eeg_WT      = []
            eeg_prom    = []

            for i in range(0, np.size(channel) - nWindow, noverlap):            
                
                # Calculo entropía wavelet
                eeg_WT.append(ent.wEntropy(channel[i:i+nWindow], base, level)) 
                    
                # Promedio señal
                eeg_prom.append(channel[i:i+nWindow].mean())
            
            # Convierto a np.array()
            eeg_prom    = np.array(eeg_prom)
            eeg_WT      = np.array(eeg_WT)
                
            # Grafico resultados
            aux.graficar_entropy(eeg_prom, eeg_WT)
              
    except IndexError:
        print(f"Numero de canal inválido")



if __name__ == '__main__':
    # python3 tp_final.py 'eeg_epilepsia.mat' 2
    if len(sys.argv) <= 3:
        
        try:
            if len(sys.argv) == 1:
                archivo = 'eeg_epilepsia.mat'
                n_canal = None
            elif len(sys.argv) == 2:
                archivo = sys.argv[1]
                n_canal = None   
            else:
                archivo = sys.argv[1]
                n_canal = int(sys.argv[2])

            main(archivo, n_canal)
                
        except FileNotFoundError:
            print(f'No existen los archivos en el ordenador')
    
    else:
        print(f'Mal argumentos')    
        


    
    
