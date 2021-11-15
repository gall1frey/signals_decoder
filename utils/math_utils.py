from math import *
from cmath import polar

def rect_to_polar(x,y):
	r = x+y*1j
	return polar(r)

def polar_to_rect(rho,phi):
	i = rho*cos(phi)
	q = rho*sin(phi)
	return (i,q)

def dist_bw_points(point1, point2):
	x1,y1 = point1
	x2,y2 = point2
	return sqrt(pow((x1-x2),2)+pow((y1-y2),2))

def degrees_to_rad(angle):
	return radians(angle)

def rad_to_degrees(angle):
	return degrees(angle)
