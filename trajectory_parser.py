#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Modified date: 14/03/2016
# Jim, Nima
#

import numpy as np
import scipy as sp

import PyKEP as pk

import date
import position
import velocity

class TrajectoryParser:
    """Class permitting to read, recover and return the contents of a file of trajectory.

    The file should have as format a list of data without containing any string. The class
    TrajectoryParser uses following classes as association class: Date, Position and Velocity.
    Recovered data are:
    -d: represents an epoch (a fixed point in time)
    -p: the position vector of the spacecraft
    -v: the velocity vector of the spacecraft.

    """
    def __init__(self):
	"""Constructor of the class TrajectoryParser."""
	self.d = date.Date()
	self.p = position.Position()
	self.v = velocity.Velocity()
    def parse_trajectory(self, trajectory_file):
	"""Method reading the contents of a specified trajectory file and returning the
	data as a list of epoch, an array of position vector and an array of velocity vector.
	"""
	for line in trajectory_file.read().splitlines():
	    values = [float(element) for element in line.split(' ')]
	    self.d.dates.append(values[0])
	    #p.position_vector.append([values[1], values[2], values[3]])
	    self.p.x.append(values[1])
	    self.p.y.append(values[2])
	    self.p.z.append(values[3])
	    #v.velocity_vector.append([values[4], values[5], values[6]])
	    self.v.vx.append(values[4])
	    self.v.vy.append(values[5])
	    self.v.vz.append(values[6])
	#self.p.position_vector = np.array(self.p.position_vector) * 1000
	self.p.x = np.array(self.p.x) * 1000
	self.p.y = np.array(self.p.y) * 1000
	self.p.z = np.array(self.p.z) * 1000
	#self.v.velocity_vector = np.array(self.v.velocity_vector)
	self.v.vx = np.array(self.v.vx) 
	self.v.vy = np.array(self.v.vy) 
	self.v.vz = np.array(self.v.vz) 
        return self.d.dates, self.p.x, self.p.y, self.p.z, self.v.vx, self.v.vy, self.v.vz
