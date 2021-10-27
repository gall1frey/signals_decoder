# -*- coding: utf-8 -*-
"""
Author: Gallifrey
"""

import matplotlib.pyplot as plt
import numpy as np
from math import pi
#import gen_binary as gb

class FSK:
	def __init__(self,sampling_freq=1000,carrier_freq=50,symbol_duration=0.1,data=''):
		self.sampling_freq = sampling_freq
		self.carrier_freq = carrier_freq
		self.symbol_duration = symbol_duration
		self.data = data
		self.total_time = len(self.data)*8*self.symbol_duration
		self.t = np.arange(0,self.total_time,1/self.sampling_freq)
		self.symbol_length = int(self.symbol_duration*self.sampling_freq)
		self.no_of_symbols = int(np.floor(np.size(self.t)/self.symbol_length))

	def modulate(self):
		binary_signal = self.get_binary_signal()
		f = self.carrier_freq + self.carrier_freq*binary_signal/2
		fsk = np.sin(2*pi*f*self.t)
		return fsk

	def recompute(self):
		self.total_time = len(self.data)*8*self.symbol_duration
		self.t = np.arange(0,self.total_time,1/self.sampling_freq)
		self.no_of_symbols = int(np.floor(np.size(self.t)/self.symbol_length))
		self.symbol_length = int(self.symbol_duration*self.sampling_freq)

	def set_sampling_freq(self,freq):
		self.sampling_freq = freq
		self.recompute()

	def set_carrier_freq(self,freq):
		self.carrier_freq = freq
		self.recompute()

	def set_symbol_duration(self,t):
		self.symbol_duration = t
		self.recompute()

	def data(self,data):
		self.data = data
		self.recompute()

	def get_binary_signal(self,random=False):
		if random == True:
			rand_n = np.random.rand(self.no_of_symbols)
			rand_n[np.where(rand_n >= 0.5)] = 1
			rand_n[np.where(rand_n < 0.5)] = 0
		else:
			rand_n = []
			for i in self.data.encode():
				for j in bin(i)[2:]:
					rand_n.append(int(j))
			rand_n = np.array(rand_n)
		sig = np.zeros(self.symbol_length*self.no_of_symbols)
		id_n = np.where(rand_n == 1)
		for i in id_n[0]:
			temp = int(i*self.symbol_length)
			sig[temp:temp+self.symbol_length] = 1
		return sig

def save_as_iq(signal,file_path):
	## TODO: Add checks to ensure correct datatype
	signal = signal.astype(np.complex64)
	signal.tofile(file_path)

f = FSK(1000,50,0.1,'CTF{FL4G}')
bin_sig = f.get_binary_signal()
print(bin_sig)
fsk = f.modulate()
save_as_iq(fsk,'ssd.iq')

plt.subplot(211)
plt.plot(f.t,bin_sig)
plt.title('random_binary_waveform')
plt.xlabel('time in seconds')
plt.ylabel('amplitude')


plt.subplot(212)
plt.plot(f.t,fsk)
plt.plot(f.t,bin_sig)
plt.title('fsk signal')
plt.xlabel('time in seconds')
plt.ylabel('amplitude')
plt.tight_layout()

plt.show()
