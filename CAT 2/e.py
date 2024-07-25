import numpy as np
import matplotlib.pyplot as plt

# Define the sampling rate and duration
sampling_rate = 1000  # in Hz
duration = 1          # in seconds

# Define the time vector
t = np.linspace(0, duration, sampling_rate * duration, endpoint=False)

# Define the frequencies
f1 = 50  # in Hz
f2 = 120  # in Hz

# Define the signal
s = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)

# Compute the FFT
fft_s = np.fft.fft(s)
fft_freqs = np.fft.fftfreq(len(fft_s), 1 / sampling_rate)

# Plot the signal
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, s)
plt.title('Original Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# Plot the FFT
plt.subplot(2, 1, 2)
plt.plot(fft_freqs[:len(fft_freqs)//2], np.abs(fft_s[:len(fft_s)//2]))
plt.title('FFT of the Signal')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')
plt.grid()
plt.tight_layout()
plt.show()
