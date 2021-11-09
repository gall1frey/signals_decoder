import numpy as np
from math import sqrt,log,degrees

class QAM_CONSTELLATIONS:
	def __init__(self,bits_per_sample=4,amplitude = 1):
		if log(2**bits_per_sample,4) != int(log(2**bits_per_sample,4)):
			raise ValueError('bits_per_sample must be a power of 4!')
		self.bits_per_sample = bits_per_sample
		self.points_on_axis = sqrt(2**self.bits_per_sample)
		self.bits_per_quadrant = self.points_on_axis//2
		self.amplitude = amplitude

	def get_constellation_map(self):
		axis = []
		jump = self.amplitude/self.bits_per_quadrant
		marker = jump
		while marker <= self.amplitude:
			axis.extend([marker,-marker])
			marker += jump
		axis.sort(reverse=True)
		rev_axis = axis[::-1]
		format_str = '{:0'+str(self.bits_per_sample//2)+'b}'
		constellation = dict()
		for x in range(len(rev_axis)):
			for y in range(len(axis)):
				a = format_str.format(y)+format_str.format(x)
				constellation[a] = self.rect_to_polar(rev_axis[x],axis[y])
		return constellation

	def rect_to_polar(self,x,y):
		rho = np.sqrt(x**2 + y**2)
		phi = degrees(np.arctan2(y, x))
		return(rho, phi)

class PSK_CONSTELLATIONS:
	def __init__(self,bits_per_sample=2,amplitude=1):
		self.bits_per_sample = bits_per_sample
		self.amplitude = amplitude
		self.total_angle = 360

	def get_constellation_map(self):
		angle_jump = self.total_angle/(2**self.bits_per_sample)
		constellation = {}
		no = 0
		phase = 0
		format_str = '{:0'+str(self.bits_per_sample)+'b}'
		while phase < self.total_angle:
			constellation[format_str.format(no)] = (self.amplitude,phase)
			no += 1
			phase += angle_jump
		return constellation

if __name__ == '__main__':
	## DEBUG: This section only for debugging
	bps = 16
	q = QAM_CONSTELLATIONS(bits_per_sample=bps).get_constellation_map()
	print(q,len(q)==bps)
