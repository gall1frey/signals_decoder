# -*- coding: utf-8 -*-
"""
	Authors: Gallifrey

	This file contains signal utilities. These include functions to generate
	sine waves, square waves, fast fourier transforms and dealing with iq and wav files

	Some functions are incomplete
"""

import numpy as np
from math import pi

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
		Only supports no. of symbols = 2
	'''
	#Define the jump at which to sample square wave
	jump = int(sampling_freq*symbol_duration)
	#Sample the wave
	data = np.array([sig[x] for x in range(0,len(sig),jump)])
	data[data == -1] = 0
	return data.astype(int)

def get_fft(signal):
	'''
		Returns the fast fourier transform of a signal
	'''
	return np.fft.fft(signal)

def windowing(signal,t):
	return signal * np.hamming(t)
