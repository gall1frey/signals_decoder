import numpy as np
class dataUtils:
	def get_random_data(num_symbols):
		'''
			Generates a random array of length num_symbols
			Currently only generates an array of two kinds of symbols
			(0,1). Needs to be modified to generate an array of any number of symbols
		'''
		return np.random.randint(0, 2, num_symbols)*2-1

	def get_binary_array_from_Data(data):
		'''
			Given a string, converts it into a binary array
		'''
		arr = []
		for i in data.encode():
			for j in '{:08b}'.format(i):
				arr.append(int(j))
		arr = np.array(arr)
		return arr

	def get_data_from_binary_array(array):
		'''
			Given a binary array, returns strings from it
		'''
		bytes = [array[i:i+8] for i in range(0,len(array),8)]
		chars = []
		for i in bytes:
			tmp = ''
			for j in i:
				tmp += str(int(j))
			chars.append(chr(int(tmp,2)))
		return ''.join(chars)
