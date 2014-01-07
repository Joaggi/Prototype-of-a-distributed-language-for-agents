# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 23:51:37 2013

@author: Alejandro
"""
import Pyro4
from Agente import Agente
from Servicio import Servicio
from ComunidadAgentes import ComunidadAgentes


Ingenieros = ComunidadAgentes("estudiantes")
#Metodo pyro
#Se crea de la manera simple con serveSimple, sin tener en cuenta el host.
Pyro4.Daemon.serveSimple({
    Ingenieros : "agentes.distribuidos.comunidad." + str(Ingenieros.getNombre())
},host="192.168.1.14")

