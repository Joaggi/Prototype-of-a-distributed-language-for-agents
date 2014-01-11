# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:49:14 2013

@author: Alejandro Gallego Hola mundo
"""
import Pyro4
import threading
import time

class Agente(object):
    """"""
    
    tipoMovilidad = ["constante","uniforme","exponencial"]    
    
    def __init__(self,nombre, movilidadId, racionalidadId, hostUri):
        ""
        self.hostUri = hostUri
        self.nombre = nombre
        self.movilidadId = movilidadId
        self.racionalidadId = racionalidadId
        thread = threading.Thread(target = self.wait2Seconds, args = [])
        thread.start()

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

    def disperseMySelf(self):
        return Pyro4.Proxy(self.hostUri).disperseAgente(self.nombre)

    def printSomething(self):
        print('hola')

    def wait2Seconds(self):
        time.sleep(2)
        print('hello')
        self.disperseMySelf()