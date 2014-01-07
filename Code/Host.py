# -*- coding: utf-8 -*-
"""
Created on Mon Dec 09 21:39:36 2013

@author: Alejandro
"""
import Pyro4

# we're using custom classes, so need to use pickle
Pyro4.config.SERIALIZER='pickle'

# we're using custom classes, so need to use pickle
Pyro4.config.SERIALIZERS_ACCEPTED.add('pickle')


class Host(object):
    """Esta clase se encargara de todas las funciones de 
    definicion del ..."""
    
    def __init__(self , nombre):   
        self.nombre = nombre
        self.listNS = {}
        self.listAgentes = {}
        self.listMovilidad = {}
        self.listRacionalidad = {}
    
    def getNombre(self):
        """ """
        return self.nombre
    
    def getListNS(self):
        """ Se obtiene la lista de los naming space que define pyro
        en ellos se encuentra la direccion de cada uno de los hosts
        que se encuentran esparcidos en la red ad-hoc"""
        return self.listNS;
        
    def addNS(self,host,ns):
        """    """
        try:
            if self.listNS[host]:
                print "El NS existe en la lista"
        except KeyError:
            self.listNS[host] = "PYRO:Pyro.NameServer@" + str(host)  +":"+ str(ns.port)
            
    def setListNS(self, lNS):
        self.listNS = lNS
        
    def deleteNS(self,nombre):
        """    """
        try:
            del self.listNS[nombre]
            print "Se elimino el NS de la lista"
        except KeyError:
            print "No existe el NS en la lista"
        
    def getListAgentes(self):  
        """  """
        return self.listAgentes;
    
    def addAgente(self,agente):
        """ """
        try:
            if self.listAgentes[agente.getNombre()]:
                print "El Agente existe en la lista"
        except KeyError:
            self.listAgentes[agente.getNombre()] = agente
    
    def setListAgente(self, lAgente):
        self.listAgente = lAgente
        
    def deleteAgente(self,nombre):
        """ """
        try:
            del self.listAgente[nombre]
            print "Se elimino el Agente de la lista"
        except KeyError:
            print "No existe el Agente en la lista"
        
            
    def getListMovilidad(self,):
        """ """
        return self.listMovilidad;
        
    def addMovilidad(self,movilidad):
        """ """
        try:
            if self.listMovilidad[movilidad.getNombre()]:
                print "La movilidad existe en la lista"
        except KeyError:
            self.listMovilidad[movilidad.getNombre()] = movilidad

    def setListMovilidad(self, lMovilidad):
        self.listMovilidad = lMovilidad
        
    def deleteMovilidad(self,nombre):
        """ """
        try:
            del self.listMovilidad[nombre]
            print "Se elimino la movilidad de la lista"
        except KeyError:
            print "No existe la movilidad en la lista"
        
            
    def getListRacionalidad(self,):
        """ """
        return self.listRacionalidad;
        
    def addRacionalidad(self,racionalidad):
        """ """
        try:
            if self.listRacionalidad[racionalidad.getNombre()]:
                print "La racionalidad existe en la lista"
        except KeyError:
            self.listRacionalidad[racionalidad.getNombre()] = racionalidad
        
    def setListRacionalidad(self, lRacionalidad):
        self.listRacionalidad = lRacionalidad
            
    def deleteRacionalidad(self,nombre):
        """ """
        try:
            del self.listRacionalidad[nombre]
            print "Se elimino la racionalidad de la lista"
        except KeyError:
            print "No existe la racionalidad en la lista"
        
    
    