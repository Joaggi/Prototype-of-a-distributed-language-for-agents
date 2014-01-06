# -*- coding: utf-8 -*-
"""
Created on Mon Dec 09 21:45:18 2013

@author: Alejandro
"""
import Pyro4

# we're using custom classes, so need to use pickle
Pyro4.config.SERIALIZER='pickle'

# we're using custom classes, so need to use pickle
Pyro4.config.SERIALIZERS_ACCEPTED.add('pickle')


class Movilidad(object):
    """ Se define la movilidad de los agentes. """
    
    def __init__(self):
        """Se inicializa la clase """
        self.movilidad = {}
        
    def setMovilidad(self,nombreMovilidad,parametros):
        """    """
        self.movilidad[nombreMovilidad] = parametros
        
    def getMovilidad(self):
        """    """
        return self.movilidad