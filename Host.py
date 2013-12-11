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
    
    def __init__(self ):   
        self.listNS = {}
        self.listAgentes = {}
        self.listMovilidad = {}
        self.listRacionalidad = {}
        
    
    def getListNS(self):
        """ Se obtiene la lista de los naming space que define pyro
        en ellos se encuentra la direccion de cada uno de los hosts
        que se encuentran esparcidos en la red ad-hoc"""
        return self.listNS;
        
    def addNS(self,ns):
        """    """
        self.listNS[ns.getNombre()] = ns
        
    def deleteNS(self,nombre):
        """    """
        del self.listNS[nombre]
        
    def getListAgentes(self):  
        """  """
        return self.listAgentes;
    
    def addAgente(self,agente):
        """ """
        self.listAgentes[agente.getNombre()] = agente
        
    def deleteAgente(self,nombre):
        """ """
        del self.listAgente[nombre]
            
    def getListMovilidad(self,):
        """ """
        return self.listMovilidad;
        
    def addMovilidad(self,movilidad):
        """ """
        self.listMovilidad[movilidad.getNombre()] = movilidad

    def deleteMovilidad(self,nombre):
        """ """
        del self.listMovilidad[nombre]
            
    def getListRacionalidad(self,):
        """ """
        return self.listRacionalidad;
        
    def addRacionalidad(self,racionalidad):
        """ """
        self.listRacionalidad[racionalidad.getNombre()] = racionalidad
            
    def deleteRacionalidad(self,nombre):
        """ """
        del self.listRacionalidad[nombre]
    
    