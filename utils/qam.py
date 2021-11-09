import numpy as np
from matplotlib import pyplot as plt
from .signal import Signal

class QAM(Signal):
	def __init__(self,
			modulation = {'0':(0,0), '1':(1,0)},
			sampling_freq = 10,
			bits_per_sample = 1,
			carrier_freq = 100):
		'''
		Create a modulator using OOK by default
		'''
		self.modulation    = modulation
		self.baud_rate     = baud_rate
		self.bits_per_baud = bits_per_baud
		self.carrier_freq  = carrier_freq

	def generate_signal(self, data):
		'''
		Generate signal corresponding to the current modulation scheme to
		represent given binary string, data.
		'''
		def create_func(data):
			slot_data = []
			for i in range(0,len(data),self.bits_per_sample):
				slot_data.append(self.modulation[data[i:i+self.bits_per_sample]])
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
		return duration, func
