# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:49:14 2013

@author: Alejandro Gallego
"""
#

from Agente import Agente
from Servicio import Servicio

import Pyro4

# we're using custom classes, so need to use pickle
Pyro4.config.SERIALIZER='pickle'

# we're using custom classes, so need to use pickle
Pyro4.config.SERIALIZERS_ACCEPTED.add('pickle')



class ComunidadAgentes(object):
    """ """
    idAgente = 1
    def __init__(self,nombre):
        """Constructor de la clase comunidad de agentes. """
        self.__nombre = nombre
        ComunidadAgentes.idAgente+=1
        self.agente = {}
        
    def setServicio(self,servicio):
        """ Se asigna un servicio, de la clase Servicio, a la comunidad de agentes """
        print "Inicializo servicio"
        self.servicio = servicio
        
    def getServicio(self):
        """ """
        return self.servicio
        
    def getNombre(self):
        """ """
        return self.__nombre
        
    def addAgente(self,agente,nombre):
        """ """
        self.agente[nombre] = agente
        
    def getAgente(self,nombre):
        """ """
        return self.agente[nombre]
