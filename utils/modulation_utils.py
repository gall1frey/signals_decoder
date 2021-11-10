import numpy as np
from matplotlib import pyplot as plt
from .signal import Signal

class QAM:
	def __init__(self,modulation = {'0':(0,0), '1':(1,0)},sampling_freq = 10,bits_per_sample = 1,carrier_freq = 100):
		self.modulation = modulation
		self.sampling_freq = sampling_freq
		self.bits_per_sample = bits_per_sample
		self.carrier_freq = carrier_freq

	def generate_signal(self, data):
		'''
		Generate signal corresponding to the current modulation scheme to
		represent given binary string, data.
		'''
		def create_func(data):
			slot_data = []
			for i in range(0,len(data),self.bits_per_sample):
				try:
					slot_data.append(self.modulation[data[i:i+self.bits_per_sample]])
				except:
					slot_data.append(self.modulation[data[i:i+self.bits_per_sample]+'0'*(self.bits_per_sample-len(data[i:i+self.bits_per_sample]))])
			def timefunc(t):
				slot = int(t*self.sampling_freq)
				start = float(slot)/self.sampling_freq
				offset = t - start
				amplitude,phase = slot_data[slot]
				return amplitude*np.sin(2*np.pi*self.carrier_freq*offset +
					phase/180.0*np.pi)
			return timefunc
		func = create_func(data)
		duration = float(len(data))/(self.sampling_freq*self.bits_per_sample)
		s = Signal(total_time=duration, func=func)
		return s

	def get_constellations(self):
		data = [(a*np.cos(p/180.0*np.pi), a*np.sin(p/180.0*np.pi), t)
				for t,(a,p) in self.modulation.items()]
		return data

def split_data(data,bits):
	data = list(data)
	if len(data) % bits != 0:
		data.extend([0 for i in range(bits - (len(data) % bits))])
	data1 = ''
	data2 = ''
	for i in range(0,len(data),bits):
		data1 += ''.join([str(j) for j in data[i:i+bits//2]])
		data2 += ''.join([str(j) for j in data[i+bits//2:i+bits]])
	return data1,data2

class FSK:
	def __init__(self,sampling_freq = 10,bits_per_sample = 1,carrier_freq = 100,amplitude=1):
		self.sampling_freq = sampling_freq
		self.bits_per_sample = bits_per_sample
		self.carrier_freq = carrier_freq
		self.amplitude = amplitude

	def generate_signal(self,data):
		def create_func(data):
			slot_data = []
			for i in range(0,len(data),self.bits_per_sample):
				slot_data.extend(list(str(data[i])*self.bits_per_sample))
			slot_data = np.array(slot_data).astype(int)
			slot_data = slot_data*2-1
			def timefunc(t):
				return self.amplitude*np.sin(2*np.pi*(self.carrier_freq+self.carrier_freq*slot_data[int(t)]/2)*t)
			return timefunc
		func = create_func(data)
		duration = float(len(data))/(self.sampling_freq*self.bits_per_sample)
		s = Signal(total_time=duration, func=func)
		return s
'''
	class sigUtils:
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
'''
