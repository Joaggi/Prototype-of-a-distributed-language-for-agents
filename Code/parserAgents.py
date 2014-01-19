import grammar as g
import re
import threading
import InicializacionNaming
import time
import Pyro4

init=InicializacionNaming.Inicializacion()

def analizarSintaxis(all_tokens):
	p=re.compile(g.getDeclaraciones())
	i=1
	for token_list in all_tokens:
		if p.match(" ".join(token_list))==None:
			print "Error de sintaxis en la linea %d" %(i)
			return False
		elif token_list[0]=="iniciar_programa":
			iniciar_programa()
		elif token_list[0]=="detener_programa":
			detener_programa()
		elif token_list[0]=="crear_agente":
			crear_agente(token_list[1][1:-1])
		elif token_list[0]=="eliminar_agente":
			eliminar_agente(token_list[1][1:-1])
		elif token_list[0]=="recuperar_agente":
			recuperar_agente(token_list[1][1:-1])
		elif token_list[0]=="dispersar_agente":
			dispersar_agente(token_list[1][1:-1])
		elif token_list[0]=="crear_comunidad":
			crear_comunidad(token_list[1][1:-1])
		elif token_list[0]=="iniciar_servicio":
			iniciar_servicio(token_list[1][1:-1])
		elif token_list[0]=="detener_servicio":
			detener_servicio(token_list[1][1:-1])
		i+=1

def iniciar_programa():
    thread = threading.Thread(target = init.initialize, args=[])
    thread.start()
    while(init.isReady()==False):
        print "Inicializando..."
        time.sleep(0.5)
    print "Inicializacion terminada!"
    
def detener_programa():
	init.setRunning(False)

def crear_agente(nombre):
	host = Pyro4.Proxy(Pyro4.locateNS().list().values()[1])
	host.addAgente(nombre)
	print "Agente %s agregado a la red!" % (nombre)

def eliminar_agente(nombre):    
	host = Pyro4.Proxy(Pyro4.locateNS().list().values()[1])  
	agente = Pyro4.Proxy(host.resolve(nombre)) 
	agente.stopThread()  
	Pyro4.Proxy(agente.getHostUri()).deleteAgente(nombre)  
	movilidadUri = host.resolve("legs_" + nombre)
	racionalidadUri = host.resolve("arms_" + nombre)
 	print "7"    
	try:
		ns = Pyro4.locateNS(host = movilidadUri[movilidadUri.find("@")+1:movilidadUri.find(":",5)])
		host = Pyro4.Proxy(ns.list().values()[1])
		host.deleteMovilidad("legs_" + nombre)
	except:
		print "No se pudo eliminar la movilidad del agente dado que no se encontro"
	try:
		ns = Pyro4.locateNS(host = racionalidadUri[movilidadUri.find("@")+1:movilidadUri.find(":",5)])
		host = Pyro4.Proxy(ns.list().values()[1])
		host.deleteRacionalidad("arms_" + nombre)
	except:
		print "No se pudo eliminar la movilidad del agente dado que no se encontro"
      

def recuperar_agente(nombre):
	host = Pyro4.Proxy(Pyro4.locateNS().list().values()[1])
	print "El agente %s esta en: %s" %(nombre,host.retrieveAgente(nombre))
	
def dispersar_agente(nombre):
	host = Pyro4.Proxy(Pyro4.locateNS().list().values()[1])
	Pyro4.Proxy(host.resolve(nombre)).doIt()
	print "El agente %s esta en: %s" %(nombre,host.disperseAgente(nombre))

def crear_comunidad(nombre):
	host = Pyro4.Proxy(Pyro4.locateNS().list().values()[1])
	host.addComunidadAgentes(nombre)
	print "Comunidad %s agregado a la red!" % (nombre) 
	
def iniciar_servicio(nombre):
	print "Ejecutar comando para iniciar el servicio: "+nombre
	
def detener_servicio(nombre):
	print "Ejecutar comando para detener el servicio: "+nombre
