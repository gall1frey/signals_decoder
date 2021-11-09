from .file_utils import fileUtils
from scipy.fftpack import fft, ifft
import numpy as np

class Signal(fileUtils):
	def __init__(self, total_time=1.0, sampling_freq=22050, func=None):
		'''
		Initialize a signal object with the specified total_time (in seconds)
		and sampling frequency (in Hz).  If func is provided, signal
		data will be initialized to values of this function for the entire
		total_time.
		'''
		self.total_time = total_time
		self.sampling_freq = sampling_freq
		self.signal = np.arange(int(total_time*sampling_freq), dtype=complex)
		self.signal[:] = 0j
		if func is not None:
			self.sample_time_function(func)

	def get_sampling_freq(self):
		'''
		Return the sampling frequency associated with the signal in Hz
		'''
		return self.sampling_freq

	def get_total_time(self):
		'''
		Return the total_time of the signal in seconds
		'''
		return self.total_time

	def amplify(self, factor):
		'''
		Amplify the signal by the specified factor
		'''
		self.signal *= factor

	def clear(self, cond=lambda f:True):
		'''
		Set amplitudes of all frequencies satisfying the condition, cond, to
		zero, where cond is a boolean function that takes a frequency in Hz.
		'''
		n = len(self.signal)
		for i in range(n):
			# convert index to corresponding frequency value
			f = float(i)*self.sampling_freq/n
			if cond(f):
				self.signal[i] = 0j

	def set_freq(self, freq, amplitude, phase=0):
		'''
		Set a particular frequency component with the specified amplitude and
		phase-shift (in degree) to the signal
		'''
		n = len(self.signal)
		index = int(np.round(float(freq)*n/self.sampling_freq))
		re = float(n)*amplitude*np.cos(phase*np.pi/180.0)
		im = float(n)*amplitude*np.sin(phase*np.pi/180.0)
		if freq != 0:
			re = re/2.0
			im = im/2.0
			self.signal[ index] = re + 1j*im
			self.signal[-index] = re - 1j*im
		else:
			self.signal[index] = re + 1j*im

	def sample_time_function(self, func):
		'''
		Sample values from a time-domain, real-valued function, func(t), where
		t will be specified in second.  Samples are collected at the
		sampling frequency associated with the Signal object.
		'''
		n = len(self.signal)
		signal = np.arange(n, dtype=float)
		for i in range(n):
			signal[i] = func(float(i)/self.sampling_freq)
		self.signal = fft(signal)

	def square_wave(self, freq, flimit=8000):
		'''
		Generate a band-limited square wave on to the signal object
		'''
		self.clear()
		f = freq
		while f <= flimit:
			self.set_freq(f, 1.0/f, -90)
			f += 2*freq

	def get_time_domain(self):
		'''
		Return a tuple (X,Y) where X is an array storing the time axis,
		and Y is an array storing time-domain representation of the signal
		'''
		x_axis = np.linspace(0, self.total_time, len(self.signal))
		y_axis = ifft(self.signal).real
		return x_axis, y_axis

	def get_frequency_domain(self):
		'''
		Return a tuple (X,A,P) where X is an array storing the frequency axis
		up to the Nyquist frequency (excluding negative frequency), and A and
		P are arrays storing the amplitude and phase shift (in degree) of each
		frequency
		'''
		n = len(self.signal)
		num_freqs = int(np.ceil((n+1)/2.0))
		x_axis = np.linspace(0, self.sampling_freq/2.0, num_freqs)
		a_axis = abs(self.signal[:num_freqs])/float(n)
		p_axis = np.arctan2(
					self.signal[:num_freqs].imag,
					self.signal[:num_freqs].real) * 180.0/np.pi
		a_axis[1:] = a_axis[1:]*2
		return x_axis, a_axis, p_axis

	def shift_freq(self, offset):
		'''
		Shift signal in the frequency domain by the amount specified by offset
		(in Hz).  If offset is positive, the signal is shifted to the right
		along the frequency axis.  If offset is negative, the signal is
		shifted to the left along the frequency axis.
		'''
		n = len(self.signal)
		nyquist = n/2
		offset = int(np.round(float(offset)*n/self.sampling_freq))
		if abs(offset) > nyquist:
			raise Exception(
			'Shifting offset cannot be greater than the Nyquist frequency')
		if offset > 0:
			self.signal[offset:nyquist] = np.copy(self.signal[:nyquist-offset])
			self.signal[:offset] = 0
			self.signal[-nyquist+1:-offset] = np.copy(self.signal[-(nyquist-offset)+1:])
			self.signal[-offset+1:] = 0
		else:
			offset = -offset
			self.signal[:nyquist-offset] = np.copy(self.signal[offset:nyquist])
			self.signal[nyquist-offset:nyquist] = 0
			self.signal[-(nyquist-offset)+1:] = np.copy(self.signal[-nyquist+1:-offset])
			self.signal[-nyquist+1:-nyquist+offset] = 0

	def shift_time(self, offset):
		'''
		Shift signal in the time domain by the amount specified by offset
		(in seconds).  If offset is positive, the signal is shifted to the
		right along the time axis.  If offset is negative, the signal is
		shifted to the left along the time axis.
		'''
		noff = offset*self.sampling_freq
		x,y = self.get_time_domain()
		if noff > 0:
			y[noff:] = y[:len(x)-noff].copy()
			y[:noff] = 0.0
		elif noff < 0:
			noff = -noff
			y[:len(x)-noff] = y[noff:].copy()
			y[len(x)-noff:] = 0.0
		self.signal = fft(y)

	def windowing(self,algorithm='hamming'):
		if algorithm == 'hamming':
			return self.signal * np.hamming(len(self.signal))

	def copy(self):
		'''
		Clone the signal object into another identical signal object.
		'''
		s = Signal()
		s.total_time = self.total_time
		s.sampling_freq = self.sampling_freq
		s.signal = np.array(self.signal)
		return s

	def mix(self, signal):
		'''
		Mix the signal with another given signal.  sampling frequency and total_time
		of both signals must match.
		'''
		if self.sampling_freq != signal.sampling_freq \
			or len(self.signal) != len(signal.signal):
			raise Exception(
				'Signal to mix must have identical sampling frequency and total_time')
		self.signal += signal.signal

	def gaussian_filter(self,signal):
		pass

	def __add__(self, s):
		newSignal = self.copy()
		newSignal.mix(s)
		return newSignal
