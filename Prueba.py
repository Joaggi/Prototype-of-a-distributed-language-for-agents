# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 23:51:37 2013

@author: Alejandro
"""

#Prueba
import Pyro4
from Agente import Agente
from Servicio import Servicio

ns = Pyro4.locateNS()
print (ns.list(prefix="agentes.distribuidos.comunidad.").items())

comunidadAgentes = Pyro4.core.Proxy("PYRONAME:agentes.distribuidos.comunidad.ingenieros")
comunidadAgentes.addAgente(Agente("Joseph"),"Joseph")

comunidadAgentes = Pyro4.core.Proxy("PYRONAME:agentes.distribuidos.comunidad.ingenieros")
comunidadAgentes.setServicio(Servicio("Skype"))

print(comunidadAgentes.getServicio().getNombre())


