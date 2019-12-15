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
fc = 11500  # Frequência de corte
w = fc / (fs / 2)  # Normalização

# Cria o filtro
b, a = scipy.signal.butter(20, w, 'low')

# Executa o Filtro no sinal
output = scipy.signal.filtfilt(b, a, audioBruto)

sinal2 = scipy.signal.hilbert(output)

# Faz a transformada de fourier
frequencia = np.fft.rfft(np.abs(sinal2))

wav.write('saida.wav', 44100, abs(sinal2))

# # Gráfico da Mensagem
# plt.title('Mensagem')
plt.plot(abs(sinal2))
# plt.xlabel('Tempo')
# plt.ylabel('Amplitude')
plt.grid(True)

plt.show()
