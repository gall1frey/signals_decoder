# -*- coding: utf-8 -*-
"""
Authors: Gallifrey
"""

#Yet to fill this in
if __name__ == '__main__':
	# ONLY FOR DEBUGGING
	from visualizer import Visualizer, graphData
	from data_utils import dataUtils
	sampling_freq = 1000
	carrier_freq = 50
	symbol_duration = 0.1
	t_duration = 100
	barr = dataUtils.get_binary_array_from_Data('Sample_data')
	binary_signal, total_time = generate_binary_waveform(barr,symbol_duration,sampling_freq)
	carrier = generate_carrier_signal(carrier_freq,generate_t(total_time,sampling_freq))
	ask = carrier * binary_signal

	g = graphData(generate_t(total_time,sampling_freq),ask,'time','freq')

	demodulated = ask[1:]/carrier[1:]
	Visualizer.plot_waves([g])
	barr = get_binary_data_from_square_wave(symbol_duration,sampling_freq,demodulated)
	decoded = dataUtils.get_data_from_binary_array(barr)
	print(decoded)
