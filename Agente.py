# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:49:14 2013

@author: Alejandro Gallego Hola mundo
"""
import Pyro4
from Movilidad import Movilidad
from Racionalidad import Racionalidad

# we're using custom classes, so need to use pickle
Pyro4.config.SERIALIZER='pickle'

# we're using custom classes, so need to use pickle
Pyro4.config.SERIALIZERS_ACCEPTED.add('pickle')


class Agente(object):
    tipoMovilidad = ["constante","uniforme","exponencial"]    
    
    def __init__(self,nombre):
        """ """
        self.nombre = nombre
        self.movilidad = Movilidad()
        

    def getNombre(self):
        """ """
        return self.nombre
        
    def setMovilidad(self,nombreMovilidad,parametros):
        """ """
        self.movilidad.setMovilidad(nombreMovilidad,parametros)

    def getMovilidad(self):
        """ """
        return self.movilidad.getMovilidad        
