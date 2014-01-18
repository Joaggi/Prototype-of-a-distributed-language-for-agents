# -*- coding: utf-8 -*-
"""
Created on Mon Dec 09 22:54:23 2013

@author: Alejandro
"""
import Pyro4
from Agente import Agente
from Servicio import Servicio
from ComunidadAgentes import ComunidadAgentes


#Prueba


ns = Pyro4.locateNS()
print (ns.list(prefix="agentes.distribuidos.comunidad.").items())

comunidadAgentes = Pyro4.core.Proxy("PYRONAME:agentes.distribuidos.comunidad.estudiantes")
print(comunidadAgentes.getAgente("Josephg").getNombre())