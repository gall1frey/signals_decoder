import numpy as np
import matplotlib.pyplot as plt

class graphData:
	def __init__(self,x,y,xlabel,ylabel):
		self.x = x
		self.y = y
		self.xlabel = xlabel
		self.ylabel = ylabel

class graphUtils:
	def plot_wave(graph_data_list,title):
		"""
			Plot waves for each val in graph_list
		"""
		for i in graph_data_list:
			#plt.subplot(3,1,graph_data_list.index(i)+1)
			plt.plot(i.x,i.y)
			plt.xlabel(i.xlabel)
			plt.ylabel(i.ylabel)
		plt.title(title)
		plt.show()

	def waterfall(wave):
		"""
			Plot waterfall
		"""
		## TODO:
		pass

	def plot_constellation(self,title,data,annotations=True,mods=False):
		"""
			Plot constellation
		"""
		if mods == True:
			sx1,sy1 = zip(data[0])
			sx2,sy2,t = zip(*data[1])
			plt.scatter(sx1,sy1,s=50)
			plt.scatter(sx2,sy2,s=10)
			plt.title(title)
			plt.xlabel('I')
			plt.ylabel('Q')
			for x,y,t in data[1]:
				plt.annotate(t,(x-.03,y-.03), ha='right', va='top')
		else:
			if annotations == False:
				sx,sy = zip(data)
			else:
				sx,sy,t = zip(*data)
			#plt.clf()
			plt.scatter(sx,sy,s=30)
			if annotations == True:
				for x,y,t in data:
					plt.annotate(t,(x-.03,y-.03), ha='right', va='top')
			#plt.axis([-1.5,1.5,-1.5,1.5])
		plt.axhline(0, color='red')
		plt.axvline(0, color='red')
		plt.grid(True)
		plt.show()
