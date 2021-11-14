import numpy as np
from scipy.io import wavfile
from scipy.fftpack import fft, ifft

class fileUtils:
	def save_to_iq(self,signal,sampling_freq,duration,file_path):
		"""
			Save signal to iq file
		"""
		if file_path [-3:] == '.iq':
			file_path = file_path[:-3]
		signal = signal.astype(np.complex64)
		signal.tofile(file_path+'.iq')
		with open(file_path+'.txt','w') as f:
			f.write('{} {}'.format(sampling_freq,duration))

	def read_from_iq(self,file_path,channel='left'):
		"""
			Read signal from iq file
		"""
		if file_path [-3:] == '.iq':
			file_path = file_path[:-3]
		sig = np.fromfile(file_path+'.iq', dtype=np.complex64)
		sampling_freq = 0
		duration = 0
		with open(file_path+'.txt','r') as f:
			sampling_freq,duration = [float(i) for i in f.read().strip().split()]
		return sampling_freq, duration, sig

	def save_to_wav(self,wave,file_path):
		"""
			Save wave to wav file
		"""
		if file_path[-4:] != '.wav':
			file_path += '.wav'

		wavfile.write(file_path,wave.sampling_freq,(ifft(wave.signal).real*32768).astype(np.dtype('int16')))

	def read_from_wav(self,file_path,channel='left'):
		"""
			Read wave from wav file
		"""
		if file_path[-4:] != '.wav':
			file_path += '.wav'
		rate,data = wavfile.read(file_path)
		n = data.shape[0]
		sampling_freq = rate
		duration = float(n)/rate
		if data.dtype == np.dtype('int16'):
			normalizer = 32768.0
		elif data.dtype == np.dtype('int8'):
			normalizer = 256.0
		else:
			raise(Exception('Unsupport data type'))
		if len(data.shape) == 2: # stereo stream
			if channel == 'left':
				data = data[:,0]
			elif channel == 'right':
				data = data[:,1]
			else:
				raise(Exception('Invalid channel choice "%s"' % channel))
		freqs = fft(data/normalizer)
		return sampling_freq, duration, freqs

	def read_from_sdr(self,dev):
		"""
			Read wave from sdr
		"""
		## TODO:

	def transmit_to_sdr(self,wave,dev):
		"""
			Transmit wave via sdr
		"""
		## TODO:
