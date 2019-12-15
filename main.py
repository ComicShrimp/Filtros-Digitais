import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
import scipy.signal

# Carrega o arquivo
audioBruto = scipy.io.loadmat('proj.mat')

# Retira somente os dados do arquivo do matlab
audioBruto = audioBruto.get('r')[0]

fs = 44100  # Frequência de amostragem
fc = 11000  # Frequência de corte baixa
fc2 = 14000  # Frequência de corte alta
w = fc / (fs / 2)  # Normalização
w2 = fc / (fs / 2)

# Cria os filtros
b, a = scipy.signal.butter(20, w, 'low')
c, d = scipy.signal.butter(20, w, 'high')

# Executa o Filtro no sinal
sinal1 = scipy.signal.filtfilt(b, a, audioBruto)
sinal2 = scipy.signal.filtfilt(c, d, audioBruto)

texto1 = scipy.signal.hilbert(sinal1)
texto2 = scipy.signal.hilbert(sinal2)

# Faz a transformada de fourier
frequencia = np.fft.rfft(np.abs(sinal2))

wav.write('saida.wav', 44100, abs(texto1))
wav.write('saida2.wav', 44100, abs(texto2))
