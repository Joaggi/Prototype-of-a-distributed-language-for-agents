# -*- coding: utf-8 -*-
"""
Created on Mon Dec 09 21:45:18 2013

@author: Alejandro
"""


class Movilidad(object):
    """ Se define la movilidad de los agentes. """

    def __init__(self, agentId):
        self.id = agentId
        self.agentId = agentId

    def getAgentId(self):
        return self.agentId

    def getId(self):
        return self.id

    def getType(self): #this should be done with some sort of parent class but whatever
        return 'legs'
    
    def sayLegs(self):
        return 'I am Legs "' + self.id + '", and I am running on ' + str(self._pyroDaemon.locationStr)