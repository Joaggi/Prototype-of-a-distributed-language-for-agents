# -*- coding: utf-8 -*-
"""
Created on Mon Dec 09 22:54:23 2013

@author: Alejandro
"""
import Pyro4
from Agente import Agente
from Servicio import Servicio
from ComunidadAgentes import ComunidadAgentes
from Host import Host

#Prueba


ns = Pyro4.locateNS()
host = Pyro4.core.Proxy("PYRONAME:agentes.distribuidos.host")

if len(host.getListNS()) != 0:    
    for naming in host.getListNS():
        print naming