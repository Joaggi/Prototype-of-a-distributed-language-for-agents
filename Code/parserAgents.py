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
			crear_agente(token_list[1])
		elif token_list[0]=="eliminar_agente":
			eliminar_agente(token_list[1])
		elif token_list[0]=="recuperar_agente":
			recuperar_agente(token_list[1])
		elif token_list[0]=="dispersar_agente":
			dispersar_agente(token_list[1])
		elif token_list[0]=="crear_comunidad":
			crear_comunidad(token_list[1])
		elif token_list[0]=="iniciar_servicio":
			iniciar_servicio(token_list[1])
		elif token_list[0]=="detener_servicio":
			detener_servicio(token_list[1])
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
	agenteURI = host.resolve(nombre)
	Pyro4.Proxy(agenteURI.getHostUri()).deleteAgente(nombre)
	movilidadUri = host.resolve("legs_" + nombre)
	try:
		ns = Pyro4.locateNS(host = movilidadUri[movilidadUri.find("@"),movilidadUri.find(":")])
		host = Proxy(ns.list().values()[1])
		host.deleteMovilidad("legs_" + nombre)
		agente = host.resolve("arms_" + nombre)
		Pyro4.Proxy(agente.getHostUri()).deleteAgente(nombre)
	except:
		print "Agente %s eliminado de la red!" %(nombre)

def recuperar_agente(nombre):
	host = Pyro4.Proxy(Pyro4.locateNS().list().values()[1])
	print "El agente %s esta en: %s" %(nombre,host.retrieveAgente(nombre))
	
def dispersar_agente(nombre):
	host = Pyro4.Proxy(Pyro4.locateNS().list().values()[1])
	print "El agente %s esta en: %s" %(nombre,host.disperseAgente(nombre))

def crear_comunidad(nombre):
	print "Ejecutar comando para crear la comunidad: "+nombre
	
def iniciar_servicio(nombre):
	print "Ejecutar comando para iniciar el servicio: "+nombre
	
def detener_servicio(nombre):
	print "Ejecutar comando para detener el servicio: "+nombre