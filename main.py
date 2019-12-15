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

plt.plot(abs(frequencia))
plt.xlabel('Frequência')
plt.ylabel('Magnitude')
plt.grid(True)
plt.show()

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

wav.write('saida.wav', 44100, abs(texto1))
wav.write('saida2.wav', 44100, abs(texto2))
