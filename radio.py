from utils.data_utils import dataUtils
from utils.signal import Signal
from utils.graph_utils import graphUtils, graphData
from utils.file_utils import fileUtils
from modulators import *
from prediction_function import Predictor
import tensorflow as tf

class Radio(QAM,dataUtils,graphUtils,graphData,fileUtils):
	def __init__(self,bits_per_sample=1,sampling_freq=10,carrier_freq=50,model_path=None):
		self.bits_per_sample = bits_per_sample
		self.sampling_freq = sampling_freq
		self.carrier_freq = carrier_freq
		super().__init__(sampling_freq=sampling_freq,bits_per_sample=bits_per_sample,carrier_freq=carrier_freq)
		self.QAM16 = QAM16
		self.QAM64 = QAM64
		self.QAM256 = QAM256
		self.BPSK = BPSK
		self.PSK8 = PSK8
		self.GFSK = GFSK
		if model_path is None:
			self.Predictor = Predictor()
		else:
			self.Predictor = Predictor(model_path)

	def get_sig_from_file(self,filetype,filepath,channel=None):
		sampling_freq = self.sampling_freq
		duration = 1
		sigarray = []
		if filetype == 'wav':
			sampling_freq, duration, sigarray = self.read_from_wav(filepath,channel)
		elif filetype == 'iq':
			sampling_freq, duration, sigarray = self.read_from_iq(filepath)
		s = Signal(total_time=duration,sampling_freq=sampling_freq)
		s.signal = sigarray
		return s

	def save_sig_to_file(self,filetype,filepath,sig):
		if filetype == 'wav':
			self.save_to_wav(sig,filepath)
		elif filetype == 'iq':
			signal = sig.signal
			duration = sig.total_time
			sampling_freq = sig.sampling_freq
			self.save_to_iq(signal,sampling_freq,duration,filepath)

	def predict_modulation(self,signal):
		if type(signal) == np.complex128:
			signal = signal.real
		return self.Predictor.predict(signal)

if __name__ == '__main__':
	"""
		Testing
	"""

	#Create a radio and data utils object
	r = Radio()
	d = dataUtils()

	#Convert string data to binary array to transmit
	#data = d.str_to_binarray('Hunger looks very like evil from the wrong end of the cutlery')
	data = d.str_to_binarray('hello')

	#Modulate
	modulated = r.GFSK(sampling_freq=10,carrier_freq=10)
	s = modulated.modulate(data)

	#Predict modulation
	#re = s.copy().signal.real[:128]
	#i = s.copy().signal.imag[:128]
	#sig = np.array([[re,i]])
	#print("PREDICTION:",r.predict_modulation(tf.expand_dims(sig, axis=-1)))

	'''
	[
		[[r1,r2,...,r128],[i1,i2,...,i128]]
		[[r1,r2,...],[i1,i2,...]]
		[[r1,r2,...],[i1,i2,...]]
	]
	'''
	#Demodulate
	demod_, samp_freq = modulated.demodulate(s,'filtered')
	demod, samp_freq = modulated.demodulate(s)

	#Convert data to string
	#print(d.binarray_to_string(demod))
	print(d.binarray_to_string(demod[::samp_freq][1:]))

	#visualize
	#graphUtils().plot_constellation('constellation map for GFSK modulation',[modulated.get_sig_constellation(s),modulated.get_constellations()],mods=True)
	#s.amplify(1.5,'baseband')
	x, y1, y2, y3 = s.get_time_domain()
	g1 = graphData(x,y1,'time','amplitude')
	#x, a, p = s.get_frequency_domain()
	#g2 = graphData(x,y3,'time','amplitude')
	g2 = graphData(x,demod,'time','amplitude')
	#g3 = graphData(x,y2,'time','amplitude')
	g3 = graphData(x,demod_,'time','amplitude')
	graphUtils.plot_wave([g1,g2,g3],'superimposed square wave for GFSK modulation')
