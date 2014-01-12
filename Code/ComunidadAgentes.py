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
    
    def __init__(self,nombre,servicioId, hostUri):
        """Constructor de la clase comunidad de agentes. """
        self.__nombre = nombre
        ComunidadAgentes.idAgente+=1
        self.agentesId = []
        self.servicioId = servicioId
        self.hostUri = hostUri
        
    def setServicio(self,servicioId):
        """ Se asigna un servicio, de la clase Servicio, a la comunidad de agentes """
        print "Inicializo servicio"
        self.servicioId = servicioId
        
    def getServicio(self):
        """ """
        return self.servicioId
        
    def getNombre(self):
        """ """
        return self.__nombre
        
    def addAgente(self,agenteId):
        """ """
        self.agentesId.append(agenteId)
        
    def getAgente(self,nombre):
        """ """
        return self.agentesId[nombre]
        
    def getListAgente(self):
        return self.agentesId
        
    def getPyroId(self):
        return str(self._pyroId)
        
    def getMeetAgente(self, precioOfrecido):
        host = Pyro4.Proxy(self.hostUri)
        for agenteId in self.getListAgente():
            agent = host.retrieveAgente(agenteId)
            if(agent!=False):
                try:
                    racionalidad = Pyro4.Proxy(host.getListRacionalidad()[Pyro4.Proxy(agent).getRacionalidadId()])
                    if (racionalidad.funcionUtilidad() <= precioOfrecido):
                        print "Este agente cooperara"
                    
                except:
                    "El agente no tiene racionalidad, por lo tanto no se puede negociar"
                
                