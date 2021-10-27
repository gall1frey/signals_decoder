def save_as_iq(signal,file_path):
	'''
		Save waveform to an iq file
	'''
	## TODO: Add checks to ensure correct datatype
	signal = signal.astype(np.complex64)
	signal.tofile(file_path)

def read_from_iq(file_path):
	'''
		Read dignal from an iq file
	'''
	return np.fromfile(file_path, dtype=np.complex64)

def save_as_wav(signal,file_path):
	## TODO: Write func to save a signal to a wav file
	pass

def read_from_wav(file_path):
	## TODO: Write func to read a signal from a wav file
	pass
