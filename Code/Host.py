# -*- coding: utf-8 -*-
"""
Created on Mon Dec 09 21:39:36 2013

@author: Alejandro
"""
import Pyro4
import Agente
import Racionalidad
import Movilidad
import random

class Host(object):
    """Esta clase se encargara de todas las funciones de 
    definicion del ..."""

    def getNombre(self):
        """ """
        return self.nombre
    
    def __init__(self , nombre):   
        self.nombre = nombre
        self.listNS = {}
        self.listAgentes = {}
        self.listMovilidad = {}
        self.listRacionalidad = {}
    
    def resolve(self, name):#had to add this methos on the host, so it can act sorta like a NameServer
        ret = self.find(name)
        if(ret == False):
            print('Precaucion!: objeto no esta en el host. Esto puede afectar el rendimiento.')
            for nameServer,nameServer_uri in self.listNS.items():
                try:                
                    findHost = Pyro4.Proxy(Pyro4.Proxy(nameServer_uri).list()['host.' + self.nombre])
                    ret = findHost.find(name)
                except:
                    print "Error: no se localizo el host"
                    ret = False
                if(ret!=False):
                    return ret
        return ret


    
    def find(self, name):
        """ returns uri of object or false """
        try:
            return self.listAgentes[name]
        except:
            try:
                return self.listMovilidad[name]
            except:
                try:
                    return self.listRacionalidad[name]
                except:
                    return False    
    

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
    
    def addAgente(self,agente, create = True):
        if(self.resolve(agente) == False):
            movilidadId = 'legs_' + agente
            racionalidadId = 'arms_' + agente
            hostUri = 'PYRO:' + self._pyroId + '@' + self._pyroDaemon.locationStr
            agent = Agente.Agente(agente, movilidadId, racionalidadId, hostUri)
            if(create):
                self.addRacionalidad(racionalidadId)
                self.addMovilidad(movilidadId)

            print('Adding head ' + agent.getNombre() + ' to Daemon in ' + str(self._pyroDaemon.locationStr))
            uri = self._pyroDaemon.register(agent)
            self.listAgentes[agent.getNombre()] = uri.asString()
            return uri.asString()
        else:
            #Corregir
            return self.resolve(agente)

    def setListAgente(self, lAgente):
        self.listAgentes = lAgente
        
    def deleteAgente(self,nombre):
        uri = self.listAgentes[nombre]
        print('Removing ' + nombre + ' from Daemon at ' + self._pyroDaemon.locationStr)
        self._pyroDaemon.unregister(uri[5:uri.find('@')])
        self.listAgentes.pop(nombre)
            
    def getListMovilidad(self):
        """ """
        return self.listMovilidad;
        
    def addMovilidad(self,movilidadId): 
        movilidad = Movilidad.Movilidad(movilidadId)
        print('Adding Movility ' + movilidad.getId() + ' to Daemon in ' + str(self._pyroDaemon.locationStr))
        uri = self._pyroDaemon.register(movilidad)
        self.listMovilidad[movilidad.getId()] = uri.asString()

    def setListMovilidad(self, lMovilidad):
        self.listMovilidad = lMovilidad
        
    def deleteMovilidad(self,nombre):
        uri = self.listMovilidad[nombre]
        print('Removing ' + nombre + ' from Daemon at ' + self._pyroDaemon.locationStr)
        self._pyroDaemon.unregister(uri[5:uri.find('@')])
        self.listMovilidad.pop(nombre)
            
        
            
    def getListRacionalidad(self):
        return self.listRacionalidad

        
    def addRacionalidad(self,racionalidadId):
        racionalidad = Racionalidad.Racionalidad(racionalidadId)
        print('Adding rationality ' + racionalidad.getId() + ' to Daemon in ' + str(self._pyroDaemon.locationStr))
        uri = self._pyroDaemon.register(racionalidad)
        self.listRacionalidad[racionalidad.getId()] = uri.asString()
        
    def setListRacionalidad(self, lRacionalidad):
        self.listRacionalidad = lRacionalidad
            
    def deleteRacionalidad(self,nombre):
        uri = self.listRacionalidad[nombre]
        print('Removing ' + nombre + ' from Daemon at ' + self._pyroDaemon.locationStr)
        self._pyroDaemon.unregister(uri[5:uri.find('@')])
        self.listRacionalidad.pop(nombre)
     
    def moveAgente(self, nombre, hostTo):  
        try:
            uri = self.listAgentes[nombre]
            print('Moviendo ' + nombre + ' to ' + hostTo + '...')
            self.deleteAgente(nombre)
            newHost = Pyro4.Proxy(Pyro4.locateNS(hostTo).list()['host.' + self.nombre])
            return newHost.addAgente(nombre, False)
        except:
            print('No existe el agente en este Host')

    def moveMovilidad(self, nombre, hostTo):  
        try:
            uri = self.listMovilidad[nombre]
            print('Moviendo ' + nombre + ' to ' + hostTo + '...')
            self.deleteMovilidad(nombre)
            newHost = Pyro4.Proxy(Pyro4.locateNS(hostTo).list()['host.' + self.nombre])
            newHost.addMovilidad(nombre)
        except:
            print('No existe la movilidad en este Host')

    def moveRacionalidad(self, nombre, hostTo):  
        try:
            uri = self.listRacionalidad[nombre]
            print('Moviendo ' + nombre + ' to ' + hostTo + '...')
            self.deleteRacionalidad(nombre)
            newHost = Pyro4.Proxy(Pyro4.locateNS(hostTo).list()['host.' + self.nombre])
            newHost.addRacionalidad(nombre)
        except:
            print('No existe la racionalidad en este Host')

    def disperseAgente(self, agentId):
        agent = Pyro4.Proxy(self.listAgentes[agentId])
        movilidadId = agent.getMovilidadId()
        racionalidadId = agent.getRacionalidadId()
        self.moveMovilidad(movilidadId, random.sample(self.listNS.keys(), 1)[0])
        self.moveRacionalidad(racionalidadId, random.sample(self.listNS.keys(), 1)[0])
        return self.moveAgente(agentId, random.sample(self.listNS.keys(), 1)[0])
        
        
    #Servicio
    def searchHead(self, name):#had to add this methos on the host, so it can act sorta like a NameServer
        ret = self.findHead(name)
        if(ret == False):
            print('Precaucion!: Head del objeto no esta en el host. Esto puede afectar el rendimiento.')
            for nameServer,nameServer_uri in self.listNS.items():
                try:                
                    findHost = Pyro4.Proxy(Pyro4.Proxy(nameServer_uri).list()['host.' + self.nombre])
                    ret = findHost.findHead(name)
                except:
                    print "Error: no se localizo el host"
                    ret = False
                if(ret != False):
                    return [ret,Pyro4.Proxy(nameServer_uri).list()['host.' + self.nombre]]
        return ret
        
    
    def findHead(self, name):
        """ returns uri of object or false """
        try:
            return self.listAgentes[name]
        except:
            return False   
            
    def searchMovilidad(self, name):#had to add this methos on the host, so it can act sorta like a NameServer
        ret = self.findMovilidad(name)
        if(ret == False):
            print('Precaucion!: Movilidad del objeto no esta en el host. Esto puede afectar el rendimiento.')
            for nameServer,nameServer_uri in self.listNS.items():
                try:                
                    findHost = Pyro4.Proxy(Pyro4.Proxy(nameServer_uri).list()['host.' + self.nombre])
                    ret = findHost.findMovilidad(name)
                except:
                    print "Error: no se localizo el host"
                    ret = False
                if(ret != False):
                    return [ret,Pyro4.Proxy(nameServer_uri).list()['host.' + self.nombre]]
        return ret

    
    def findMovilidad(self, name):
        """ returns uri of object or false """
        try:
            return self.listMovilidad[name]
        except:
            return False   
            
    def searchRacionalidad(self, name):#had to add this methos on the host, so it can act sorta like a NameServer
        ret = self.findRacionalidad(name)
        if(ret == False):
            print('Precaucion!: Movilidad del objeto no esta en el host. Esto puede afectar el rendimiento.')
            for nameServer,nameServer_uri in self.listNS.items():
                try:                
                    findHost = Pyro4.Proxy(Pyro4.Proxy(nameServer_uri).list()['host.' + self.nombre])
                    ret = findHost.findRacionalidad(name)
                except:
                    print "Error: no se localizo el host"
                    ret = False
                if(ret != False):
                    return ret
        return ret
        
    
    def findRacionalidad(self, name):
        """ returns uri of object or false """
        try:
            return self.listRacionalidad[name]
        except:
            return False     
    
    #Funciones para la comunidad de agentes.
    def retrieveAgente(self, agentId):
        #Primero se recupera la cabeza o encabezado del agente.
        agent = self.searchHead(agentId)
        if(agent == False):
            print 'No se encontro el agente'
        else:
            print 'Moviendo el encabezado al host ' + self.nombre
            agent = self.moveAgente(agentId,self.listNS[self.nombre])
            movilidadId = Pyro4.Proxy(agent).getMovilidadId()
            [movilidad,hostMovilidad] = self.searchMovilidad(movilidadId)
            if(movilidad == False):
                print 'No se encontro la movilidad '
                print 'Dado que no se encontro la movilidad no se procedera a encontrar la racionalidad'
            else:
                self.moveMovilidad(movilidadId, self.listNS[self.nombre])
                racionalidadId = Pyro4.Proxy(agent).getRacionalidadId()
                try:
                    Pyro4.Proxy(hostMovilidad).getListMovilidad()[racionalidadId]
                    self.moveRacionalidad(racionalidadId,self.listNS[self.nombre])
                except:
                    'La racionalidad no se encuentra con la movilidad por lo tanto no se podra mover'
                    
        return agent