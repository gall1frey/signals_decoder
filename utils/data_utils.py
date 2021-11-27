import numpy as np
import string

class dataUtils:
	def generate_random_data(self,num_bits):
		"""
			Generate random binarray of num_bits bits
		"""
		return np.random.randint(0, 2, num_symbols)*2-1

	def str_to_binarray(self,data,encoding_callback=None):
		"""
			Convert data string to binary array
		"""
		binarray = []
		for i in data.encode():
			for j in '{:08b}'.format(i):
				binarray.append(int(j))
		if encoding_callback != None:
			binarray = encoding_callback(binarray,func='encode')
		binarray = np.array(binarray)
		return binarray

	def binarray_to_string(self,binarray,encoding_callback=None):
		"""
			Convert binary array to data string
		"""
		data = []
		if encoding_callback != None:
			binarray = encoding_callback(binarray,func='decode')
		bytes = [binarray[i:i+8] for i in range(0,len(binarray),8)]
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
			for i in binarray:
				if i == 1:
					op_array.extend([1,0])
				else:
					op_array.extend([0,1])
		elif func == 'decode':
			for i in range(0,len(binarray),2):
				tmp = binarray[i:i+2]
				if tmp[0] == 0 and tmp[1] == 1:
					op_array.append(0)
				else:
					op_array.append(1)
		return op_array

	def diff_manchester(self,binarray,func='encode'):
		"""
			Encode or decode differential manchester
		"""
		op_array = []
		differential = {
			(1,0): [0,1],
			(0,0): [1,0],
			(0,1): [1,1],
			(1,1): [0,0],
		}
		init_level = 1
		if func == 'encode':
			for bit in binarray:
				op_array.extend(differential[(init_level, bit)])
				init_level = op_array[-1]
		elif func == 'decode':
			symbols = binarray
			while len(symbols):
				symbol = symbols[0:2]
				symbols = symbols[2:]
				for ib, s in differential.items():
					if symbol[0] == s[0] and symbol[1] == s[1]:
						op_array.append(ib[1])
		return op_array

	def nrz_i(self,binarray,func='encode'):
		"""
			Encode or decode NonReturnZero
		"""
		op_array = []
		init = 1
		if func == 'encode':
			if binarray[0] == 1:
				op_array.append(int(not init))
			else:
				op_array.append(int(init))
			for i in range(1,len(binarray)):
				if binarray[i] == 0:
					op_array.append(int(op_array[i-1]))
				else:
					op_array.append(int(not op_array[i-1]))
		elif func == 'decode':
			if binarray[0] != init:
				op_array.append(1)
			else:
				op_array.append(0)
			for i in range(1,len(binarray)):
				if binarray[i] != binarray[i-1]:
					op_array.append(1)
				else:
					op_array.append(0)
		return op_array

	def nrz_l(self,binarray,func='encode'):
		"""
			Encode or decode NonReturnZero
		"""
		op_array = []
		if func == 'encode' or func == 'decode':
			for i in binarray:
				op_array.append(int(not i))
		return op_array

	def find_sync(self,binarray):
		"""
			Find the SYNC word of a signal
		"""
		#Find length of sig:
		start = binarray[0:8]
		bin_list = [binarray[i:i+8] for i in range(0,len(binarray),8)]
		total_bytes = bin_list[1:].index(start)
		total_bits = (total_bytes+1)*8
		max_score = 0.0
		sync = ''
		for i in range(0,total_bits):
			b = ''.join(binarray[(i+j)%total_bits] for j in range(total_bits))
			bytes = [chr(int(b[j:j+8],2)) for j in range(8,len(b),8) if chr(int(b[j:j+8],2)) in string.printable]
			score = len(bytes)/total_bytes
			if score > max_score:
				max_score = score
				sync = b[0:8]
		return max_score,hex(int(sync,2))[2:]

	def decode_with_sync(self,binarray,sync):
		"""
			Decode a binary array using sync word (in hex)
		"""
		start = binarray[0:8]
		bin_list = [binarray[i:i+8] for i in range(0,len(binarray),8)]
		total_bytes = bin_list[1:].index(start)
		total_bits = (total_bytes+1)*8
		max_score = 0.0
		msg = ''
		for i in range(0,total_bits):
			b = ''.join(binarray[(i+j)%total_bits] for j in range(total_bits))
			if b[0:8] == bin(int(sync,16))[2:]:
				bytes = [chr(int(b[j:j+8],2)) for j in range(8,len(b),8) if chr(int(b[j:j+8],2)) in string.printable]
				score = len(bytes)/total_bytes
				if score > max_score:
					max_score = score
					msg = ''.join(bytes)
		#return max_score,hex(int(sync,2))[2:]
		return msg
