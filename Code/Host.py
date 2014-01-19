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
import ComunidadAgentes

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
        self.listComunidadAgentes = {}
    
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
        
    def addNS(self,ip,ns):
        """    """
        try:
            if self.listNS[ip]:
                print "El NS existe en la lista"
        except KeyError:
            self.listNS[ip] = "PYRO:Pyro.NameServer@" + str(ip)  +":"+ str(ns.port)
            
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
        


    #Funciones para la comunidad de agentes.
    def retrieveAgente(self, agentId):
        agenteURI = self.resolve(agentId)
        if (agenteURI == False):
            print 'El agente no se pudo encontrar'
            return False
        racionalidadId = Pyro4.Proxy(agenteURI).getRacionalidadId()
        racionalidadUri = self.resolve(racionalidadId)

        movilidadId = Pyro4.Proxy(agenteURI).getMovilidadId()
        agenteHost = agenteURI[agenteURI.find('@') + 1:]
        racionalidadHost = racionalidadUri[racionalidadUri.find('@') + 1:]
        selfHost = self._pyroDaemon.locationStr
        print 'agente: ' + agenteHost + ', racionalidad: ' + racionalidadHost + ', self: ' + selfHost
        if (racionalidadUri == False):
            print 'La racionalidad no se pudo encontrar'
            return False
        if (str(racionalidadHost) != str(agenteHost) or str(agenteHost) != str(selfHost)):
            print 'Cabeza o racionalidad no son locales'
            # buscar la movilidad en la red y recoger las partes localmente
            movilidadUri = self.resolve(movilidadId)
            if(movilidadUri == False):
                print 'Cabeza o racionalidad no son locales y la movilidad no se encuentra'
                return False
            print 'Movilidad encontrada'
            # proceder a mover las partes
            movilidadHost = movilidadUri[movilidadUri.find('@') + 1:]
            # mover la cabeza (si no es local)
            print 'Moviendo cabeza...'
            if(agenteHost != selfHost):
                remoteHost = Pyro4.Proxy(Pyro4.locateNS(agenteHost[:agenteHost.find(':')]).list()['host.' + self.nombre])
                remoteHost.moveAgente(agentId, selfHost[:selfHost.find(':')])
            #mover la racionalidad (si no es local)
            print 'Moviendo racionalidad...'
            if(racionalidadHost != selfHost):
                remoteHost = Pyro4.Proxy(Pyro4.locateNS(racionalidadHost[:racionalidadHost.find(':')]).list()['host.' + self.nombre])
                remoteHost.moveRacionalidad(racionalidadId, selfHost[:selfHost.find(':')])
            #mover la movilidad (si no es local)
            print 'Moviendo movilidad...'
            if(movilidadHost != selfHost):
                remoteHost = Pyro4.Proxy(Pyro4.locateNS(movilidadHost[:movilidadHost.find(':')]).list()['host.' + self.nombre])
                remoteHost.moveMovilidad(movilidadId, selfHost[:selfHost.find(':')])
            return self.retrieveAgente(agentId) ## una llamada resursiva, hara la verificacion de paso. Como ya esta todo local, no debe haber overhead problems
        if (str(racionalidadHost) == str(agenteHost) and str(agenteHost) == str(selfHost)):
            print 'Cabeza y racionalidad si son locales'
            return [agenteURI, racionalidadUri]
            # retoranr las uris.
        return False



        # #     print 'Moviendo el encabezado al host ' + self.nombre
        # #     agent = self.moveAgente(agentId,self.listNS[self.nombre])
        # #     movilidadId = Pyro4.Proxy(agent).getMovilidadId()
        # #     movilidad = self.resolve(movilidadId)
        # #     hostMovilidad = Pyro4.Proxy(movilidad[movilidad.find('@'),movilidad.find(':')])
        # #     if(movilidad == False):
        # #         print 'No se encontro la movilidad '
        # #         print 'Dado que no se encontro la movilidad no se procedera a encontrar la racionalidad'
        # #     else:
        # #         self.moveMovilidad(movilidadId, self.listNS[self.nombre])
        # #         racionalidadId = Pyro4.Proxy(agent).getRacionalidadId()
        # #         try:
        # #             Pyro4.Proxy(hostMovilidad).getListMovilidad()[racionalidadId]
        # #             self.moveRacionalidad(racionalidadId,self.listNS[self.nombre])
        # #         except:
        # #             'La racionalidad no se encuentra con la movilidad por lo tanto no se podra mover'
                    
        # return agent





    def getListComunidadAgentes(self):  
        """  """
        return self.listComunidadAgentes;
    
    def addComunidadAgentes(self,comunidad, create = True):
        if(self.resolve(comunidad) == False):
            hostUri = 'PYRO:' + self._pyroId + '@' + self._pyroDaemon.locationStr
            comunidad = ComunidadAgentes.ComunidadAgentes(comunidad,hostUri)
            print('Adding head ' + comunidad.getNombre() + ' to Daemon in ' + str(self._pyroDaemon.locationStr))
            uri = self._pyroDaemon.register(comunidad)
            self.listComunidadAgentes[comunidad.getNombre()] = uri.asString()
            return uri.asString()
        else:
            #Corregir
            return self.resolve(comunidad)

    def setListComunidadAgentes(self, lComunidadAgentes):
        self.listComunidadAgentes = lComunidadAgentes
        
    def deleteComunidadAgentes(self,nombre):
        uri = self.listComunidadAgentes[nombre]
        print('Removing ' + nombre + ' from Daemon at ' + self._pyroDaemon.locationStr)
        self._pyroDaemon.unregister(uri[5:uri.find('@')])
        self.listComunidadAgentes.pop(nombre)