# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 23:51:37 2013

@author: Alejandro
"""
import Pyro4
from Agente import Agente

from Host import Host


Host = Host()
#Metodo pyro
#Se crea de la manera simple con serveSimple, sin tener en cuenta el host.
Pyro4.Daemon.serveSimple({
    Host : "agentes.distribuidos.host"
},host="192.168.1.10")

