# -*- coding: utf-8 -*-
"""
Created on Mon Dec 09 21:46:17 2013

@author: Alejandro
"""

class Racionalidad(object):
	
    
    
	def __init__(self, agentId):
		self.id = agentId
		self.agentId = agentId

	def getAgentId(self):
		return self.agentId

	def getId(self):
		return self.id

	def getType(self): #this should be done with some sort of parent class but whatever
		return 'arms'

	def sayArms(self):
		return 'I am Arms "' + self.id + '", and I am running on ' + str(self._pyroDaemon.locationStr)
  
	def funcionUtilidad(self):
		return 5