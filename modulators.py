from utils.modulation_utils import QAM, split_data
from utils.constellations import QAM_CONSTELLATIONS, PSK_CONSTELLATIONS

class QAM16(QAM):
	def __init__(self,sampling_freq = 10,carrier_freq = 9.9e3):
		self.bits_per_sample = 4
		self.modulation = QAM_CONSTELLATIONS(bits_per_sample=self.bits_per_sample).get_constellation_map()
		self.q1 = QAM(sampling_freq=sampling_freq,bits_per_sample=self.bits_per_sample,carrier_freq=carrier_freq,modulation=self.modulation)
		self.q2 = QAM(sampling_freq=sampling_freq,bits_per_sample=self.bits_per_sample,carrier_freq=carrier_freq,modulation=self.modulation)

	def modulate(self,binarray):
		data1,data2 = split_data(binarray,bits=self.bits_per_sample)
		return self.q1.generate_signal(data1) + self.q2.generate_signal(data2)

	def demodulate(self):
		pass

class QAM64(QAM):
	def __init__(self,sampling_freq = 10,carrier_freq = 9.9e3):
		self.bits_per_sample = 6
		self.modulation = QAM_CONSTELLATIONS(bits_per_sample=self.bits_per_sample).get_constellation_map()
		self.q1 = QAM(sampling_freq=sampling_freq,bits_per_sample=self.bits_per_sample,carrier_freq=carrier_freq,modulation=self.modulation)
		self.q2 = QAM(sampling_freq=sampling_freq,bits_per_sample=self.bits_per_sample,carrier_freq=carrier_freq,modulation=self.modulation)

	def modulate(self,binarray):
		data1,data2 = split_data(binarray,bits=self.bits_per_sample)
		return self.q1.generate_signal(data1) + self.q2.generate_signal(data2)

	def demodulate(self):
		pass

class QAM256(QAM):
	def __init__(self,sampling_freq = 10,carrier_freq = 9.9e3):
		self.bits_per_sample = 8
		self.modulation = QAM_CONSTELLATIONS(bits_per_sample=self.bits_per_sample).get_constellation_map()
		self.q1 = QAM(sampling_freq=sampling_freq,bits_per_sample=self.bits_per_sample,carrier_freq=carrier_freq,modulation=self.modulation)
		self.q2 = QAM(sampling_freq=sampling_freq,bits_per_sample=self.bits_per_sample,carrier_freq=carrier_freq,modulation=self.modulation)

	def modulate(self,binarray):
		data1,data2 = split_data(binarray,bits=self.bits_per_sample)
		return self.q1.generate_signal(data1) + self.q2.generate_signal(data2)

	def demodulate(self):
		pass

class BPSK(QAM):
	def __init__(self,sampling_freq = 10,carrier_freq = 9.9e3):
		self.bits_per_sample = 1
		self.modulation = PSK_CONSTELLATIONS(bits_per_sample=self.bits_per_sample).get_constellation_map()
		self.q1 = QAM(sampling_freq=sampling_freq,bits_per_sample=self.bits_per_sample,carrier_freq=carrier_freq,modulation=self.modulation)

	def modulate(self,binarray):
		data = ''.join([str(i) for i in binarray])
		return self.q1.generate_signal(data)

	def demodulate(self):
		pass

class PSK8(QAM):
	def __init__(self,sampling_freq = 10,carrier_freq = 9.9e3):
		self.bits_per_sample = 3
		self.modulation = PSK_CONSTELLATIONS(bits_per_sample=self.bits_per_sample).get_constellation_map()
		self.q1 = QAM(sampling_freq=sampling_freq,bits_per_sample=self.bits_per_sample,carrier_freq=carrier_freq,modulation=self.modulation)

	def modulate(self,binarray):
		data = ''.join([str(i) for i in binarray])
		return self.q1.generate_signal(data)

	def demodulate(self):
		pass

class GFSK():
	def __init__(self,sampling_freq = 10,carrier_freq = 9.9e3,bits_per_sample=1):
		self.bits_per_sample = bits_per_sample
		self.sampling_freq = sampling_freq
		self.carrier_freq = carrier_freq
		self.q1 = QAM(sampling_freq=sampling_freq,bits_per_sample=self.bits_per_sample,carrier_freq=carrier_freq)

	def modulate(self,binarray):
		data = ''.join([str(i) for i in binarray])
		return self.q1.generate_signal(data)
