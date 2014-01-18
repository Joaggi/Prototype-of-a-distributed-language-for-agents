# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 23:37:40 2013

@author: Alejandro
"""
import Pyro4

# we're using custom classes, so need to use pickle
Pyro4.config.SERIALIZERS_ACCEPTED.add('pickle')

#Pyro4.naming.startNSloop(host = "0.0.0.0")
Pyro4.naming.startNSloop(host = "192.168.1.10")