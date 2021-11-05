from .file_utils import fileUtils
from .signal_utils import sigUtils
import numpy as np

class Signal(fileUtils,sigUtils):
	def __init__(self, total_time=1.0, sampling_freq=22050, func=None):
		self.total_time = total_time
		self.sampling_freq = sampling_freq
		self.wave = np.arange(int(total_time*sampling_freq), dtype=complex)
		self.wave[:] = 0j
		if func is not None:
			self.sample_time_function(func)

	def square_wave(self,freq,flimit):
		self.filter_freq(self.sampling_freq,self.wave)
		f = freq
		while f <= flimit:
			self.set_freq(f, 1.0/f, -90)
			f += 2*freq
		return self.wave

	def get_sampling_rate(self):
		#Get sampling frequency of signal in hertz
		return self.sampling_freq

	def get_total_time(self):
		return self.total_time

	def set_freq(self, freq, amplitude, phase=0):
		"""
		Set a particular frequency component with the specified amplitude and
		phase-shift (in degree) to the signal
		"""
		n = len(self.wave)
		index = int(np.round(float(freq)*n/self.sampling_freq))
		re = float(n)*amplitude*np.cos(phase*np.pi/180.0)
		im = float(n)*amplitude*np.sin(phase*np.pi/180.0)
		if freq != 0:
			re = re/2.0
			im = im/2.0
			self.wave[ index] = re + 1j*im
			self.wave[-index] = re - 1j*im
		else:
			self.wave[index] = re + 1j*im
