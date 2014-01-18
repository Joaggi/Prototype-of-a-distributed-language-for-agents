# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 23:51:37 2013

@author: Alejandro
"""
import Pyro4
from Agente import Agente
from Servicio import Servicio
from ComunidadAgentes import ComunidadAgentes
from Host import Host



HostLogik = Host("Logik")
#Metodo pyro
#Se crea de la manera simple con serveSimple, sin tener en cuenta el host.
Pyro4.Daemon.serveSimple({
    HostLogik : "host." + str(HostLogik.getNombre())
},host="0.0.0.0")

