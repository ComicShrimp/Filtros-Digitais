import scipy.io
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
import scipy.signal

# Carrega o arquivo
audioBruto = scipy.io.loadmat('proj.mat')

# Retira somente os dados do arquivo do matlab
audioBruto = audioBruto.get('r')[0]

fs = 44100  # Frequência de amostragem
fc = 12000  # Frequência de corte
w = fc / (fs / 2)  # Normalização

# Cria o filtro
b, a = scipy.signal.butter(10, w, 'low')

# Executa o Filtro no sinal
output = scipy.signal.filtfilt(b, a, audioBruto)

# Faz a transformada de fourier
frequencia = np.fft.rfft(output)

# # Gráfico da Mensagem
# plt.title('Mensagem')
plt.plot(abs(frequencia))
# plt.xlabel('Tempo')
# plt.ylabel('Amplitude')
plt.grid(True)

plt.show()
