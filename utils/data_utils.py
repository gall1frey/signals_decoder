import numpy as np

class dataUtils:
	def str_to_binarray(self,data):
		"""
			Convert data string to binary array
		"""
		binarray = []
		## TODO:
		return binarray

	def binarray_to_string(self,binarray):
		"""
			Convert binary array to data string
		"""
		data = ''
		## TODO:
		return data

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
