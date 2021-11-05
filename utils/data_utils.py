import numpy as np

class dataUtils:
	def generate_random_data(self,num_bits):
		"""
			Generate random binarray of num_bits bits
		"""
		return np.random.randint(0, 2, num_symbols)*2-1

	def str_to_binarray(self,data):
		"""
			Convert data string to binary array
		"""
		binarray = []
		for i in data.encode():
			for j in '{:08b}'.format(i):
				binarray.append(int(j))
		binarray = np.array(binarray)
		return binarray

	def binarray_to_string(self,binarray):
		"""
			Convert binary array to data string
		"""
		data = []
		bytes = [array[i:i+8] for i in range(0,len(array),8)]
		for i in bytes:
			tmp = ''
			for j in i:
				tmp += str(int(j))
			data.append(chr(int(tmp,2)))
		return ''.join(data)

	def manchester(self,binarray,func='encode'):
		"""
			Encode or decode manchester
		"""
		op_array = []
		if func == 'encode':
			## TODO:
			pass
		elif func == 'decode':
			## TODO:
			pass
		return op_array

	def diff_manchester(self,binarray,func='encode'):
		"""
			Encode or decode differential manchester
		"""
		op_array = []
		if func == 'encode':
			## TODO:
			pass
		elif func == 'decode':
			## TODO:
			pass
		return op_array

	def nrz(self,binarray,func='encode'):
		"""
			Encode or decode NonReturnZero
		"""
		op_array = []
		if func == 'encode':
			## TODO:
			pass
		elif func == 'decode':
			pass
			## TODO:
		return op_array
