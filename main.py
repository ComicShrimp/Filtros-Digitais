import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
from scipy.fftpack import fft
import scipy.signal

# Carrega o arquivo
audioBruto = scipy.io.loadmat('proj.mat')

# Retira somente os dados do arquivo do matlab
audioBruto = audioBruto.get('r')[0]

# Faz a transformada de fourier
frequencia = scipy.fftpack.fft(audioBruto)

plt.subplot(2, 2, 1)
plt.title('Sinal de Entrada')
plt.plot(abs(frequencia))
plt.xlabel('Frequência')
plt.ylabel('Magnitude')
plt.grid(True)

fs = 44100  # Frequência de amostragem

fc = 3900   # Frequencia de corte baixa
fc1 = 6750  # Frequência de corte alta

fc2 = 13800  # Frequencia de corte baixa
fc3 = 15750  # Frequência de corte alta

w = fc / (fs / 2)  # Normalização para radiano
w1 = fc1 / (fs / 2)

w2 = fc2 / (fs / 2)
w3 = fc3 / (fs / 2)

# Cria os filtros para aplicá-los depois
a, b = scipy.signal.butter(5, [w, w1], 'bandpass')
c, d = scipy.signal.butter(5, [w2, w3], 'bandpass')

# Aplica os ruidos
sinalSemRuido1 = scipy.signal.filtfilt(a, b, audioBruto)
sinalSemRuido2 = scipy.signal.filtfilt(c, d, audioBruto)

# Demodula os sinais
texto1 = scipy.signal.hilbert(sinalSemRuido1)
texto2 = scipy.signal.hilbert(sinalSemRuido2)

frequencia = scipy.fftpack.fft(texto1)
frequencia2 = scipy.fftpack.fft(texto2)

plt.subplot(2, 2, 2)
plt.title('Sinal 1')
plt.plot(abs(frequencia))
plt.xlabel('Frequência')
plt.ylabel('Magnitude')
plt.grid(True)

plt.subplot(2, 2, 3)
plt.title('Sinal 2')
plt.plot(abs(frequencia2))
plt.xlabel('Frequência')
plt.ylabel('Magnitude')
plt.grid(True)

# Mostra Todos os gráficos
plt.show()

# Escreve os arquivos .wav
wav.write('saida.wav', 44100, abs(texto1))
wav.write('saida2.wav', 44100, abs(texto2))
