class Visualizer:
	'''
		# TODO: Add other visualizers, complete waterfall
	'''
	def plot_waves(graph_data_list):
		'''
			Visualize wave signals as subplots on time or frequency domain
			Currently supports five plots at a time
		'''
		import matplotlib.pyplot as plt
		if len(graph_data_list) > 5:
			print("CAN'T PLOT SO MANY GRAPHS!")
			return
		if len(graph_data_list) == 1:
			plt.plot(graph_data_list[0].x_axis_array,graph_data_list[0].y_axis_array)
			plt.title('graph1')
			plt.xlabel(graph_data_list[0].xlabel)
			plt.ylabel(graph_data_list[0].ylabel)
		else:
			num_base = str(len(graph_data_list))
			num_base += '1'
			for i in range(len(graph_data_list)):
				plt.subplot(int(num_base+str(i+1)))
				plt.plot(graph_data_list[i].x_axis_array,graph_data_list[i].y_axis_array)
				plt.xlabel(graph_data_list[i].xlabel)
				plt.ylabel(graph_data_list[i].ylabel)
		plt.tight_layout()
		plt.show()

	def waterfall():
		'''
			Visualize wave signals as waterfall
		'''
		pass

class graphData:
	'''
		Class to hold data to plot
	'''
	def __init__(self,x_axis_array,y_axis_array,xlabel,ylabel):
		self.x_axis_array = x_axis_array
		self.y_axis_array = y_axis_array
		self.xlabel = xlabel
		self.ylabel = ylabel
