# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:51:42 2013

@author: Munkys
"""
import Pyro4

# we're using custom classes, so need to use pickle
Pyro4.config.SERIALIZER='pickle'

# we're using custom classes, so need to use pickle
Pyro4.config.SERIALIZERS_ACCEPTED.add('pickle')


class Servicio(object):
    
    def __init__(self,nombre):
        self.nombre = nombre
        
    def getNombre(self):
        return self.nombre