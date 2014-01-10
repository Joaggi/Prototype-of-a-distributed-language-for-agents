# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:49:14 2013

@author: Alejandro Gallego Hola mundo
"""
import Pyro4


class Agente(object):
    """"""
    
    tipoMovilidad = ["constante","uniforme","exponencial"]    
    
    def __init__(self,nombre, movilidadId, racionalidadId, hostUri):
        ""
        self.hostUri = hostUri
        self.nombre = nombre
        self.movilidadId = movilidadId
        self.racionalidadId = racionalidadId

    def getMovilidadId(self):
        return self.movilidadId

    def getRacionalidadId(self):
        return self.racionalidadId
        
    def getNombre(self):
        return self.nombre
        
    def getType(self):
        return 'head'

    def getPyroId(self):
        return str(self._pyroId)

    def doIt(self):
        ##place some call to legs and arms
        racionalidadUri = Pyro4.Proxy(self.hostUri).resolve(self.racionalidadId)
        movilidadUri =  Pyro4.Proxy(self.hostUri).resolve(self.movilidadId)
        if (racionalidadUri == False or movilidadUri == False):
            return 'Algo esta perdido'
        racionalidad = Pyro4.Proxy(racionalidadUri)
        movilidad = Pyro4.Proxy(movilidadUri)
        return [racionalidad.sayArms(), movilidad.sayLegs()]