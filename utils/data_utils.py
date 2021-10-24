import numpy as np
class dataUtils:
	def get_random_data(num_symbols):
		return np.random.randint(0, 2, num_symbols)*2-1

	def get_binary_array_from_Data(data):
		rand_n = []
		for i in data.encode():
			for j in '{:08b}'.format(i):
				rand_n.append(int(j))
		rand_n = np.array(rand_n)
		return rand_n

	def get_data_from_binary_array(array):
		bytes = [array[i:i+8] for i in range(0,len(array),8)]
		chars = []
		for i in bytes:
			tmp = ''
			for j in i:
				tmp += str(j)
			chars.append(chr(int(tmp,2)))
		return ''.join(chars)
