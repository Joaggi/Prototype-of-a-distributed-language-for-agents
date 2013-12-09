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
    #Inicializacion del objeto
    idAgente = 1
    def __init__(self,nombre):
        self.__nombre = nombre
        ComunidadAgentes.idAgente+=1
        self.agente = {}
        
    def setServicio(self,servicio):
        print "Inicializo servicio"
        self.servicio = servicio
        
    def getServicio(self):
        return self.servicio
        
    def getNombre(self):
        return self.__nombre
        
    def addAgente(self,agente,nombre):
        self.agente[nombre] = agente
        
    def getAgente(self,nombre):
        return self.agente[nombre]

Ingenieros = ComunidadAgentes("ingenieros")
#Metodo pyro
#Se crea de la manera simple con serveSimple, sin tener en cuenta el host.
Pyro4.Daemon.serveSimple({
    Ingenieros : "agentes.distribuidos.comunidad." + str(Ingenieros.getNombre())
},host="192.168.1.10")