__author__ = 'marion'
import numpy as N
import wave


class SoundFile:
    def __init__(self, signal, sample_rate):
        self.file = wave.open('../data/high_pitch_signal.wav', 'wb')
        self.signal = signal
        self.sr = sample_rate

    def write(self):
        self.file.setparams((1, 2, self.sr, self.sr * 4, 'NONE', 'noncompressed'))
        self.file.writeframes(self.signal)
        self.file.close()

# let's prepare signal
duration = 1  # seconds
sample_rate = 4410  # Hz
samples = duration * sample_rate
frequency = 500  # Hz
period = sample_rate / float(frequency)  # in sample points
omega = N.pi * 2 / period

xaxis = N.arange(int(period), dtype=N.float) * omega
ydata = 16384 * N.sin(xaxis)

signal = N.resize(ydata, (samples,))

ssignal = ''
for i in range(len(signal)):
    ssignal += wave.struct.pack('h', signal[i])  # transform to binary

f = SoundFile(ssignal, sample_rate)
f.write()
print 'file written'