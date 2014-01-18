# -*- coding: utf-8 -*-
"""
Created on Mon Dec 09 22:54:23 2013

@author: Alejandro
"""
import Pyro4
import select
from Host import Host
import time

Pyro4.config.SERIALIZERS_ACCEPTED.add('pickle')

#Prueba
nombre = "Logik"

#Al activarse la bandera no se seguira tratando de obtener el host en vez de esto se creara.
banderaNS = True
banderaHost = True

try:
    ns = Pyro4.locateNS()
except: 
    print("No existe un servidor de NS.")
    banderaNS = False
    banderaHost = False


if(banderaNS):
    try:
        hostNS = Pyro4.core.Proxy("PYRONAME:" + ns.list().keys()[1])
    except:
        print("No existe un host en este servidor de NS.")
        banderaHost = False

#Se obtiene la ip de la red.
mi_ip = Pyro4.socketutil.getIpAddress(None, workaround127=True)

print("Se procedera a crear un host")
hostDemonio = Host(nombre)


if(banderaHost):
    print("Se obtendra una lista de los ns")
    hostDemonio.setListNS(hostNS.getListNS())




print("Inicializando servicios... tipo de servidor=%s" % Pyro4.config.SERVERTYPE)
# start a name server with broadcast server as well
nameserverUri, nameserverDaemon, broadcastServer = Pyro4.naming.startNS(host="0.0.0.0")
assert broadcastServer is not None, "excepcion no se ha podido crear el servidor de broadcast"

print("Obteniendo el nombre del servidor o nameserver (ns), uri=%s" % nameserverUri)
print("Localizacion del demonio ns string=%s" % nameserverDaemon.locationStr)
print("Demonio de socket ns=%s" % nameserverDaemon.sockets)
print("Demonio de socket bc=%s (fileno %d)" % (broadcastServer.sock, broadcastServer.fileno()))
   
if(banderaHost):    
    for nameServer,nameServer_uri in hostNS.getListNS().items():
        nsDisperso = Pyro4.Proxy(nameServer_uri)
        for host, hostDisperso_uri in nsDisperso.list(prefix="host.").items():
            hostDisperso = Pyro4.Proxy(hostDisperso_uri) 
            hostDisperso.addNS(mi_ip, nameserverUri)
    
hostDemonio.addNS(mi_ip, nameserverUri)

            
#Metodo pyro
#Crear un demonio en pyro
pyrodaemon=Pyro4.core.Daemon(host=mi_ip)
print("Localizacion del demonio str=%s" % pyrodaemon.locationStr)
print("Socket del demonio=%s" % pyrodaemon.sockets)
# Se registrara un demonio en el servidor de objetos
serveruri=pyrodaemon.register(hostDemonio)
print("URI del server=%s" % serveruri)
host_proxy = Pyro4.Proxy(serveruri)

# Se registrara el demonio con el servidor embebido 
nameserverDaemon.nameserver.register("host." + nombre,serveruri)  

verificacionDeTiempo = time.time()
 


listNS = hostDemonio.getListNS().copy()
listNS.pop(mi_ip)
for host_iter,host_iter_uri in listNS.items():    
    locationHost = Pyro4.URI(host_iter_uri).location
    remoteDeamon = Pyro4.Proxy('PYRO:' + Pyro4.constants.DAEMON_NAME + '@' + locationHost)
    try:
        remoteDeamon.ping()
    except:
        print "Se ha perdido la conexion con: " + locationHost
        hostDemonio.deleteNS(locationHost[:locationHost.find(":")])
        print "prueba"
print "1"
verificacionDeTiempo = time.time()
print "2"

   
# Se crea un loop para los demonios customizado
while True:
    if(time.time()-verificacionDeTiempo >= 120):
        #Verificar conexion con host
        listNS = hostDemonio.getListNS().copy()
        listNS.pop(mi_ip)
        for host_iter,host_iter_uri in listNS.items():    
            locationHost = Pyro4.URI(host_iter_uri).location
            remoteDeamon = Pyro4.Proxy('PYRO:' + Pyro4.constants.DAEMON_NAME + '@' + locationHost)
            try:
                remoteDeamon.ping()
            except:
                print "Se ha perdido la conexion con: " + locationHost
                hostDemonio.deleteNS(locationHost[:locationHost.find(":")])
                print "prueba"
        print "1"
        verificacionDeTiempo = time.time()
        print "2"
            
                
    #Verificar 
    
    
    
    
    print("Esperando por eventos...")
    # crear un conjuto de sockets, por los cuales se estara esperando 
    # (un conjuto que provee una lista rapiada para ser comparada)
    nameserverSockets = set(nameserverDaemon.sockets)
    pyroSockets = set(pyrodaemon.sockets)
    # Solo el broadcast server es dicretamente usable como un select() objeto
    # select() se usa como un comando que espera hasta que una entrada llegue
    # esta entrada puede ser bien una entrada de IO rw, r,rw+
    rs=[broadcastServer]  
    rs.extend(nameserverSockets)
    rs.extend(pyroSockets)
    rs,_,_ = select.select(rs,[],[],3)
    eventsForNameserver=[]
    eventsForDaemon=[]
    for s in rs:
        if s is broadcastServer:
            print("Servidor de Broadcast recibio una solicitud")
            broadcastServer.processRequest()
        elif s in nameserverSockets:
            eventsForNameserver.append(s)
        elif s in pyroSockets:
            eventsForDaemon.append(s)
    if eventsForNameserver:
        print("Nameserver recibio una solicitud")
        nameserverDaemon.events(eventsForNameserver)
    if eventsForDaemon:
        print("Demonio Host recibio una solicitud")
        pyrodaemon.events(eventsForDaemon)
        


nameserverDaemon.close()
broadcastServer.close()
pyrodaemon.close()
print("done")

#if len(host.getListNS()) != 0:    
#    for naming in host.getListNS():
#        print naming