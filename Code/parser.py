import grammar as g
import re
import threading

def analizarSintaxis(all_tokens):
	p=re.compile(g.getDeclaraciones())
	i=1
	for token_list in all_tokens:
		if p.match(" ".join(token_list))==None:
			print "Error de sintaxis en la linea %d" %(i)
			return False
		elif token_list[0]=="iniciar_programa":
			iniciar_programa()
		elif token_list[0]=="crear_agente":
			crear_agente(token_list[1])
		elif token_list[0]=="mover_agente":
			mover_agente(token_list[1])
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
	thread = threading.Thread(target = iniciar_thread, args = [])
	thread.start()
	
def crear_agente(nombre):
	print "Ejecutar comando para crear el agente: "+nombre

def mover_agente(nombre):
	print "Ejecutar comando para mover el agente: "+nombre
	
def dispersar_agente(nombre):
	print "Ejecutar comando para dispersar el agente: "+nombre

def crear_comunidad(nombre):
	print "Ejecutar comando para crear la comunidad: "+nombre
	
def iniciar_servicio(nombre):
	print "Ejecutar comando para iniciar el servicio: "+nombre
	
def detener_servicio(nombre):
	print "Ejecutar comando para detener el servicio: "+nombre

def iniciar_thread():
	import InicializacionNaming
