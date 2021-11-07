#import numpy as np
from math import pi

def constellation_map_gen(basis_cpoints, basis_symbols, k, pi):
	const_points = basis_cpoints
	s = basis_symbols
	symbols = list()
	for s_i in s:
		tmp = 0
		for i,p in enumerate(pi):
			bit = (s_i >> i) & 0x1
			tmp |= bit << p
		symbols.append(tmp ^ k)
	return (const_points, symbols)

def generic_fsk_mod()

'''class sigUtils:
	def bin_data_to_signal(self,data,symbol_duration,carrier_freq,sampling_freq):
		"""
			Convert binary array to square wave
		"""
		bin_sig = []
		for i in data:
			if i == 1:
				bin_sig.extend(list(np.ones(int(sampling_freq*symbol_duration))))
			else:
				bin_sig.extend(list(np.zeros(int(sampling_freq*symbol_duration))))
		#Substitute in -1 in the signal at all indexes where
		bin_sig = np.array(bin_sig)
		bin_sig[bin_sig == 0] = -1
		total_time = len(data)*symbol_duration
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
'''
