import numpy as np
from scipy.fftpack import fft, ifft
from math import pi

class sigUtils:
	def bin_data_to_signal(self,data,symbol_duration,carrier_freq,sampling_freq):
		"""
			Convert binary array to square wave
		"""
		bin_sig = []
		for i in bin_data:
			if i == 1:
				bin_sig.extend(list(np.ones(int(sampling_freq*symbol_duration))))
			else:
				bin_sig.extend(list(np.zeros(int(sampling_freq*symbol_duration))))
		#Substitute in -1 in the signal at all indexes where
		bin_sig = np.array(bin_sig)
		bin_sig[bin_sig == 0] = -1
		total_time = len(bin_data)*symbol_duration
		return bin_sig.astype(int), total_time

	def signal_to_bin_data(self,sig,symbol_duration,carrier_freq,sampling_freq):
		"""
			Convert square wave to binary Data
		"""
		data = []
		jump = int(sampling_freq*symbol_duration)
		#Sample the wave
		data = np.array([sig[x] for x in range(0,len(sig),jump)])
		data[data == -1] = 0
		return data.astype(int)

	def analog_mod_fm(self,wave,carrier_freq,sampling_freq):
		"""
			Analog FM Modulation
		"""
		modulated = []
		## TODO:
		return modulated

	def analog_demod_fm(self,wave,carrier_freq,sampling_freq):
		"""
			Analog FM Demodulation
		"""
		demodulated = []
		## TODO:
		return demodulated

	def generate_t(self,total_time,sampling_freq,callback=None):
		"""
			Generate time array
		"""
		t = []
		if callback == None:
			t = np.arange(0,total_time,1/sampling_freq)
		else:
			pass
			## TODO: callback thing
		return t

	def generate_f(self,extreme,callback=None):
		"""
			Generate frequency array
		"""
		f = []
		if callback == None:
			f = np.arange(-extreme,extreme,1/t_duration)
		else:
			pass
			## TODO: callback thing
		return f

	def generate_sin(self,total_time,sampling_freq,carrier_freq, amp=1):
		"""
			Generate a sine wave
		"""
		wave = []
		t_array = self.generate_t(total_time,sampling_freq)
		wave = np.sin(2*pi*carrier_freq*t_array)
		return wave

	def generate_cos(self,total_time,sampling_freq,carrier_freq, amp=1):
		"""
			Generate a cosine wave
		"""
		wave = []
		t_array = self.generate_t(total_time,sampling_freq)
		wave = np.cos(2*pi*carrier_freq*t_array)
		return wave

	def filter_freq(self,sampling_freq,wave,condition=lambda f:True):
		"""
			Set amplitudes of all frequencies satisfying the condition, cond, to
			zero, where cond is a boolean function that takes a frequency in Hz.
		"""
		n = len(wave)
		for i in range(n):
			# convert index to corresponding frequency value
			f = float(i)*sampling_freq/n
			if condition(f):
				wave[i] = 0
		return wave

	def get_fft(self,signal):
		"""
			Get fast fourier transform of signal
		"""
		return fft(signal)

	def windowing(self,signal,algorithm='hamming'):
		if algorithm == 'hamming':
			return signal * np.hamming(len(signal))

	def amplify(self,factor,wave):
		return wave*factor

	def get_time_domain(self,wave,total_time):
		x_axis = np.linspace(0, total_time, len(wave))
		y_axis = ifft(wave).real
		return x_axis, y_axis

	def get_frequency_domain(self,wave,sampling_freq):
		n = len(wave)
		num_freqs = int(np.ceil((n+1)/2.0))
		x_axis = np.linspace(0, sampling_freq/2.0, num_freqs)
		a_axis = abs(wave[:num_freqs])/float(n)
		p_axis = np.arctan2(
					wave[:num_freqs].imag,
					wave[:num_freqs].real) * 180.0/np.pi
		a_axis[1:] = a_axis[1:]*2
		return x_axis, a_axis, p_axis
