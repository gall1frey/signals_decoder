class sigUtils:
	def bin_data_to_signal(self,data,symbol_duration,carrier_freq,sampling_freq):
		"""
			Convert binary array to square wave
		"""
		bin_sig = []
		## TODO:
		return bin_sig

	def signal_to_bin_data(self,sig,symbol_duration,carrier_freq,sampling_freq):
		"""
			Convert square wave to binary Data
		"""
		data = []
		## TODO:
		return data

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

	def generate_t(self,total_time,callback=None):
		"""
			Generate time array
		"""
		t = []
		## TODO:
		return t

	def generate_f(self,total_time,callback=None):
		"""
			Generate frequency array
		"""
		f = []
		## TODO:
		return f

	def gen_sin(self,total_time,sampling_freq,frequency, amp=1):
		"""
			Generate a sine wave
		"""
		wave = []
		## TODO:
		return wave

	def gen_cos(self,total_time,sampling_freq,frequency, amp=1):
		"""
			Generate a cosine wave
		"""
		wave = []
		## TODO:
		return wave

	#ADD FILTER FUNCTIONS
	def filter_abc(self):
		pass
