from .math_utils import *
import numpy as np
from .signal import Signal
from scipy.fftpack import fft, ifft

class HelperBlocks:
	def serial_to_parallel(self,data,bits_per_sample,num_outputs):
		if bits_per_sample%num_outputs != 0:
			print("INVALID INPUT")
			return
		all_outputs = [[] for i in range(num_outputs)]
		if len(data)%bits_per_sample != 0:
			data = data + '0'*(bits_per_sample-(len(data)%bits_per_sample))
		divided_data = [data[i:i+bits_per_sample] for i in range(0,len(data),bits_per_sample)]
		for i in divided_data:
			tmp = [i[x:x+int(bits_per_sample/num_outputs)] for x in range(0,len(i),int(bits_per_sample/num_outputs))]
			for j in range(len(tmp)):
				all_outputs[j].append(tmp[j])
		for i in range(len(all_outputs)):
			all_outputs[i] = ''.join(all_outputs[i])
		return all_outputs

	def parallel_to_serial(self,all_inputs,bits_per_sample):
		data = ''
		read_per_iter = len(all_inputs[0])//bits_per_sample
		for i in range(len(all_inputs)):
			all_inputs[i] = [all_inputs[i][j:j+read_per_iter] for j in range(0,len(all_inputs[i]),read_per_iter)]
		while len(all_inputs[-1]) > 0:
			for i in range(len(all_inputs)):
				data += all_inputs[i].pop(0)
		return data

	def nearest_point(self,point):
		min_dist = float('inf')
		nearest_point = '0000'
		point = (point.real,point.imag)
		modPT = None
		for i in self.modulation.keys():
			point_a, point_p = self.modulation[i]
			modpt=(polar_to_rect(point_a,point_p)[0],polar_to_rect(point_a,point_p)[1])
			dist = sqrt(pow((modpt[0]-point[0]),2)+pow((modpt[1]-point[1]),2))
			if dist < min_dist:
				min_dist = dist
				nearest_point = i
				modPT = modpt
		return nearest_point,min_dist

	def gaussian_pulse(fs,sigma):
		"""
		Generate isolated Gaussian pulse with the following parameters
		Parameters:
		fs : sampling frequency in Hz
		sigma : pulse width in seconds
		Returns:
		(t,g) : time base (t) and the signal g(t) as tuple
		Example:
		fs = 80; sigma = 0.1;
		(t,g) = gaussian_pulse(fs,sigma)
		"""
		t = np.arange(-0.5,0.5,1/fs) # time base
		g = 1/(np.sqrt(2*np.pi)*sigma)*(np.exp(-t**2/(2*sigma**2)))
		return(t,g)

class QAM(HelperBlocks):
	def __init__(self,modulation = {'0':(0,0), '1':(1,0)},sampling_freq = 10,bits_per_sample = 1,carrier_freq = 100):
		self.modulation = modulation
		self.sampling_freq = sampling_freq
		self.bits_per_sample = bits_per_sample
		self.carrier_freq = carrier_freq

	def generate_signal(self, data):
		'''
		Generate signal corresponding to the current modulation scheme to
		represent given binary string, data.
		'''
		def create_func(data):
			slot_data = []
			for i in range(0,len(data),self.bits_per_sample):
				mod_data = self.modulation[data[i:i+self.bits_per_sample]]
				slot_data.append(mod_data)
			def timefunc(t):
				slot = int(t*self.sampling_freq)
				start = float(slot)/self.sampling_freq
				offset = t - start
				amplitude,phase = slot_data[slot]
				#return I*np.cos(2*np.pi*self.carrier_freq*offset) + Q*np.sin(2*np.pi*self.carrier_freq*offset)
				return amplitude*np.sin(2*np.pi*self.carrier_freq*offset + phase)
			return timefunc
		func = create_func(data)
		duration = float(len(data))/(self.sampling_freq*self.bits_per_sample)
		s = Signal(total_time=duration, func=func)
		return s

	def get_iq_points(self,sig):
		I = []
		Q = []
		x = sig.signal
		for t in range(len(x)):
			i = x[int(t)]*np.cos(2*np.pi*self.carrier_freq*t)
			q = x[int(t)]*np.sin(2*np.pi*self.carrier_freq*t)
			#print(i,q)
			I.append(i)
			Q.append(q)
		return I,Q

	def get_constellations(self):
		data = [(a*np.cos(p), a*np.sin(p), t)
				for t,(a,p) in self.modulation.items()]
		return data

	def get_sig_constellation(self,sig):
		x = sig.baseband.copy()
		return list(x.real),list(x.imag)

	def constellation_mapper(self,data):
		slot_data = []
		for i in range(0,len(data),self.bits_per_sample):
			mod_data = self.modulation[data[i:i+self.bits_per_sample]]
			slot_data.append(mod_data)
		def timefunc(t):
			slot = int(t*self.sampling_freq)
			amplitude,phase = slot_data[slot]
			I,Q = polar_to_rect(amplitude,phase)
			return I+Q*1j
		duration = float(len(data))/(self.sampling_freq*self.bits_per_sample)
		s = Signal(total_time=duration)
		for i in range(len(s.baseband)):
			time_res = timefunc(i/s.get_sampling_freq())
			s.baseband[i] = time_res
		s.signal = self.generate_signal(data).signal
		print(s.baseband)
		s.baseband = ifft(s.baseband)
		return s

	def modulate(self,binarray):
		data = ''.join(str(i) for i in binarray)
		s = self.q1.constellation_mapper(data)
		return s

	def demodulate(self,sig):
		data = ''
		s = []
		max_amp = max(sig.baseband)
		print(max_amp)
		#sig.amplify(self.amplitude/max_amp,'baseband')
		s_ = fft(sig.baseband)
		thresh = self.amplitude/self.bits_per_sample/2
		print("NOISE THRESH:",thresh)
		for i in range(0,len(s_),int(sig.sampling_freq/self.sampling_freq)):
			if s_[i] != 0:
				pt,dist = self.nearest_point(s_[i])
				if dist < thresh:
					s.append(pt)
		sig.baseband = s_
		return ''.join(s)

class FSK:
	def __init__(self,sampling_freq = 10,bits_per_sample = 1,carrier_freq = 100,amplitude=1):
		self.sampling_freq = sampling_freq
		self.bits_per_sample = bits_per_sample
		self.carrier_freq = carrier_freq
		self.amplitude = amplitude

	def generate_signal(self,data):
		def create_func(data):
			slot_data = []
			for i in range(0,len(data),self.bits_per_sample):
				slot_data.extend(list(str(data[i])*self.bits_per_sample))
			slot_data = np.array(slot_data).astype(int)
			slot_data = slot_data*2-1
			def timefunc(t):
				return self.amplitude*np.sin(2*np.pi*(self.carrier_freq+self.carrier_freq*slot_data[int(t)]/2)*t)
			return timefunc
		func = create_func(data)
		duration = float(len(data))/(self.sampling_freq*self.bits_per_sample)
		s = Signal(total_time=duration, func=func)
		return s
