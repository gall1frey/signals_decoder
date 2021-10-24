import numpy as np
from math import pi
from visualizer import Visualizer, graphData
from data_utils import dataUtils

sampling_freq = 1000
carrier_freq = 50
symbol_duration = 0.1
t_duration = 100

def generate_t(total_time,sampling_freq):
	#Generate an array for the time axis
	return np.arange(0,total_time,1/sampling_freq)

def generate_f(extreme,t_duration):
	#Generate an array for the frequency axis
	#For plots in the frequency domain
	return np.arange(-extreme,extreme,1/t_duration)

def generate_carrier_signal(carrier_freq,t_array):
	#Generate a carrier signal given the carrier frequency and the time array
	return np.sin(2*pi*carrier_freq*t_array)

def generate_binary_waveform(bin_data,symbol_duration,sampling_freq):
	'''
		Given the data, duration of each symbol and the sampling frequency
		Generate a square wave
		This only works for any array with 0s and 1s. Probably could be modified to work for more number of symbols
		#The resulting waveform has an amplitude of 2 (cos crests are 1 and troughs are -1)
	'''
	#First create an array of all 1s. The length of this would be
	#sampling_freq times the duration of each symbol
	#bin_sig = np.ones(len(bin_data)*int(sampling_freq*symbol_duration))
	#bin_sig = np.array(list(np.ones(int(sampling_freq*symbol_duration)) if i == 1 else np.zeros(int(sampling_freq*symbol_duration)) for i in bin_data))
	bin_sig = []
	for i in bin_data:
		if i == 1:
			bin_sig.extend(list(np.ones(int(sampling_freq*symbol_duration))))
		else:
			bin_sig.extend(list(np.zeros(int(sampling_freq*symbol_duration))))
	#Substitute in -1 in the signal at all indexes where
	bin_sig = np.array(bin_sig)
	bin_sig[bin_sig == 0] = -1
	total_time = len(bin_data)*symbol_duration
	return bin_sig.astype(int), total_time

def get_binary_data_from_square_wave(symbol_duration,sampling_freq,sig):
	'''
		Gets back binary data from a square wave
	'''
	jump = int(sampling_freq*symbol_duration)
	data = np.array([sig[x] for x in range(0,len(sig),jump)])
	data[data == -1] = 0
	return data.astype(int)

def get_fft(signal):
	return np.fft.fft(signal)

def save_as_iq(signal,file_path):
	## TODO: Add checks to ensure correct datatype
	signal = signal.astype(np.complex64)
	signal.tofile(file_path)

def read_from_iq(file_path):
	return np.fromfile(file_path, dtype=np.complex64)

def windowing(signal,t):
	return signal * np.hamming(t)

if __name__ == '__main__':
	# ONLY FOR DEBUGGING
	barr = dataUtils.get_binary_array_from_Data('CTF{FL4G}')
	binary_signal, total_time = generate_binary_waveform(barr,symbol_duration,sampling_freq)
	barr = get_binary_data_from_square_wave(symbol_duration,sampling_freq,binary_signal)
	print(list(barr))
	print(dataUtils.get_data_from_binary_array(barr))
