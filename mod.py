from utils.modulation_utils import QAM, split_data

class QAM16(QAM):
	def __init__(self,sampling_freq = 10,carrier_freq = 9.9e3):
		self.bits_per_sample = 4
		self.modulation = {
			'0000' : (1.4142, 135.0000),
			'0001' : (1.1180, 116.5650),
			'0010' : (1.4142,  45.0000),
			'0011' : (1.1180,  63.4350),
			'0100' : (1.4142, 225.0000),
			'0101' : (1.1180, 243.4350),
			'0110' : (1.4142, 315.0000),
			'0111' : (1.1180, 296.5650),
			'1000' : (1.1180, 153.4350),
			'1001' : (0.7071, 135.0000),
			'1010' : (1.1180,  26.5650),
			'1011' : (0.7071,  45.0000),
			'1100' : (1.1180, 206.5650),
			'1101' : (0.7071, 225.0000),
			'1110' : (1.1180, 333.4350),
			'1111' : (0.7071, 315.0000),
		}
		self.q1 = QAM(sampling_freq=sampling_freq,bits_per_sample=self.bits_per_sample,carrier_freq=carrier_freq,modulation=self.modulation)
		self.q2 = QAM(sampling_freq=sampling_freq,bits_per_sample=self.bits_per_sample,carrier_freq=carrier_freq,modulation=self.modulation)

	def modulate(self,binarray):
		data1,data2 = split_data(binarray,bits=4)
		return self.q1.generate_signal(data1) + self.q2.generate_signal(data2)

	def demodulate(self):
		pass
