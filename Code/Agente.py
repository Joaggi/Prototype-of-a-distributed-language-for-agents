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
    LOSS = 'Algo esta perdido'
    LOSSMOVILIDAD = 'La movilidad no se encuentra!'
    
    tipoMovilidad = ["constante","uniforme","exponencial"]  
    
    tipoFuncionUtilidad = ["polinomica", ]
    
    def __init__(self,nombre, movilidadId, racionalidadId, hostUri):
        ""
        self.hostUri = hostUri
        self.nombre = nombre
        self.movilidadId = movilidadId
        self.racionalidadId = racionalidadId
        
        self.thread = threading.Thread(target = self.disperseFromMovilidad, args = [])
        self.thread.start()

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
            return Agente.LOSS
        racionalidad = Pyro4.Proxy(racionalidadUri)
        movilidad = Pyro4.Proxy(movilidadUri)
        return [racionalidad.sayArms(), movilidad.sayLegs()]

    def disperseMySelf(self):
        return Pyro4.Proxy(self.hostUri).disperseAgente(self.nombre)

    def printSomething(self):
        print('hola')

    def disperseFromMovilidad(self):
        movilidadUri =  Pyro4.Proxy(self.hostUri).resolve(self.movilidadId)
        if(movilidadUri == False):
            print Agente.LOSSMOVILIDAD
            time.sleep(2)
            self.thread = threading.Thread(target = self.disperseFromMovilidad, args = [])
            self.thread.start()
            return False
        movilidad = Pyro4.Proxy(movilidadUri)
        tiempo = movilidad.howMuchToWait()
        time.sleep(tiempo)
        self.disperseMySelf()
    
    def getHostUri(self):
        return self.hostUri
     
    def stopThread(self):
        self.thread._stop()