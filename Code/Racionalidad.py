# -*- coding: utf-8 -*-
"""
Created on Mon Dec 09 21:46:17 2013

@author: Alejandro
"""
import Pyro4

# we're using custom classes, so need to use pickle
Pyro4.config.SERIALIZER='pickle'

# we're using custom classes, so need to use pickle
Pyro4.config.SERIALIZERS_ACCEPTED.add('pickle')


class Racionalidad(object):
    """ Clase definidora de la racionalidad de los gantes. """
    
    