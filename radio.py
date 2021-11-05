from utils.data_utils import dataUtils
from utils.signal import Signal
from utils.graph_utils import graphUtils, graphData
from utils.qam import QAM

class Radio(Signal,dataUtils,graphUtils,graphData):
	def __init__(self,symbol_duration,sampling_freq):
		self.symbol_duration = symbol_duration
		self.sampling_freq = sampling_freq
		self.samples_per_symbol = sampling_freq/symbol_duration
		self.super.__init__()

if __name__ == '__main__':
	#DEBUGGING
	s = Signal()
	#sine = s.generate_sin(1,1000,50)
	sine = s.square_wave(2,flimit=50)
	#ffts = s.get_fft(sine)
	x, y = s.get_time_domain(sine,0.1)
	g1 = graphData(x,y,'x','amplitude')
	#x = s.windowing(sine)
	x,a,p = s.get_frequency_domain(sine,1000)
	g2 = graphData(x,a,'x','amplitude')
	graphUtils.plot_wave([g1,g2])
