from utils.data_utils import dataUtils
from utils.signal import Signal
from utils.graph_utils import graphUtils, graphData
from utils.file_utils import fileUtils
from utils.modulation_utils import QAM
from mod import *

class Radio(QAM,dataUtils,graphUtils,graphData,fileUtils):
	def __init__(self,bits_per_sample=1,sampling_freq=10,carrier_freq=50):
		self.bits_per_sample = bits_per_sample
		self.sampling_freq = sampling_freq
		self.carrier_freq = carrier_freq
		super().__init__(sampling_freq=sampling_freq,bits_per_sample=bits_per_sample,carrier_freq=carrier_freq)
		self.QAM16 = QAM16
		self.QAM64 = QAM64
		self.QAM256 = QAM256
		self.BPSK = BPSK
		self.PSK8 = PSK8

if __name__ == '__main__':
	#DEBUGGING
	r = Radio()
	d = dataUtils()
	data = d.str_to_binarray('Hello there, General Kenobi')
	qam16 = r.PSK8(sampling_freq=10,carrier_freq=50)
	s = qam16.modulate(data)
	graphUtils().plot_constellation(qam16.get_constellations())
	'''x, y = s.get_time_domain()
	g1 = graphData(x,y,'time','amplitude')
	x, a, p = s.get_frequency_domain()
	g2 = graphData(x,a,'freq','amplitude')
	g3 = graphData(x,p,'freq','phase')
	graphUtils.plot_wave([g1,g2,g3])'''
	#r.save_to_iq(s.signal,'modulated.iq')
