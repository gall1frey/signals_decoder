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
		## TODO:

	def read_from_wav(self,file_path):
		"""
			Read wave from wav file
		"""
		## TODO:

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
