from utils.data_utils import dataUtils
from utils.signal import Signal
from utils.graph_utils import graphUtils, graphData
from utils.qam import QAM

class Radio(Signal,dataUtils,graphUtils,graphData):
	def __init__(self,bits_per_sample=1,sampling_freq=10,carrier_freq=100):
		self.bits_per_sample = bits_per_sample
		self.sampling_freq = sampling_freq
		self.carrier_freq = carrier_freq
		self.super.__init__()

if __name__ == '__main__':
	#DEBUGGING
	'''s = Signal()
	d = dataUtils()
	s.square_wave(2,flimit=10)
	x, y = s.get_time_domain()
	g1 = graphData(x,y,'x','amplitude')
	x,a,p = s.get_frequency_domain()
	g2 = graphData(x,a,'x','amplitude')
	g3 = graphData(x,p,'x','amplitude')
	graphUtils.plot_wave([g1,g2,g3])
	'''
