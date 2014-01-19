# -*- coding: utf-8 -*-
"""
Created on Thu Jan 09 19:45:31 2014

@author: Alejandro
"""
from Pyro4 import *
host = Proxy(locateNS().list().values()[1])
agente = Proxy(host.addAgente("Jorge"))
print(agente.doIt())
host2 = Proxy(Proxy(host.getListNS().values()[0]).list().values()[1])
host.find("Jhon")
host2.resolve("Jhon")
host.disperseAgente("Jhon")
host2.getListAgentes()
agente = Proxy(host2.resolve("Jhon"))
agente = Proxy(host.resolve("Jhon"))
agente = Proxy(host.disperseAgente("Jhon"))
host.getListMovilidad()
host2.getListMovilidad()
host.getListRacionalidad()
host2.getListRacionalidad()