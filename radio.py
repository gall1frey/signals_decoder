from utils.signal_utils import sigUtils
from utils.data_utils import dataUtils
from utils.file_utils import fileUtils
from utils.graph_utils import graphUtils, graphData

class Radio(sigUtils,dataUtils,fileUtils,graphUtils,graphData):
	def __init__(self,symbol_duration,sampling_freq):
		self.symbol_duration = symbol_duration
		self.sampling_freq = sampling_freq
		self.samples_per_symbol = sampling_freq/symbol_duration
