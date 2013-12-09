# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:49:14 2013

@author: Alejandro Gallego
"""
import Pyro4


# we're using custom classes, so need to use pickle
Pyro4.config.SERIALIZER='pickle'

# we're using custom classes, so need to use pickle
Pyro4.config.SERIALIZERS_ACCEPTED.add('pickle')


class Agente(object):
    tipoMovilidad = ["constante","uniforme","exponencial"]    
    
    def __init__(self,nombre):
        self.nombre = nombre
        self.movilidad = []

    def getNombre(self):
        return self.nombre
        
    def setMovilidad(self,nombreMovilidad,parametros):
        self.movilidad[nombreMovilidad] = parametros

    def getMovilidad(self):
        return self.movilidad        