from scipy.io import wavfile
from scipy.fftpack import fft, ifft

class fileUtils:
	def save_to_iq(self,signal,file_path):
		"""
			Save signal to iq file
		"""
		signal = signal.astype(np.complex64)
		signal.tofile(file_path)

	def read_from_iq(self,file_path):
		"""
			Read signal from iq file
		"""
		return np.fromfile(file_path, dtype=np.complex64)

	def save_to_wav(self,wave,file_path):
		"""
			Save wave to wav file
		"""
		wavfile.write(wav_file,self.sampling_rate,(ifft(self.freqs).real*32768).astype(np.dtype('int16')))

	def read_from_wav(self,file_path):
		"""
			Read wave from wav file
		"""
		## TODO:
		rate,data = wavfile.read(wav_file)
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
