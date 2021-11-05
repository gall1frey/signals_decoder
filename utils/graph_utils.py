import numpy as np
import matplotlib.pyplot as plt

class graphData:
	def __init__(self,x,y,xlabel,ylabel):
		self.x = x
		self.y = y
		self.xlabel = xlabel
		self.ylabel = ylabel

class graphUtils:
	def plot_wave(self,graph_list):
		"""
			Plot waves for each val in graph_list
		"""
		for i in graph_data_list:
			plt.plot(graph_data_list[i].x_axis_array,graph_data_list[i].y_axis_array)
			plt.title('graph1')
			plt.xlabel(graph_data_list[i].xlabel)
			plt.ylabel(graph_data_list[i].ylabel)
			plt.show()

	def waterfall(self,wave):
		"""
			Plot waterfall
		"""
		## TODO:

	def plot_constellation(self,sx,sy,t):
		plt.clf()
		plt.scatter(sx,sy,s=30)
		plt.axes().set_aspect('equal')
		for x,y,t in data:
			plt.annotate(t,(x-.03,y-.03), ha='right', va='top')
		plt.axis([-1.5,1.5,-1.5,1.5])
		plt.axhline(0, color='red')
		plt.axvline(0, color='red')
		plt.grid(True)
