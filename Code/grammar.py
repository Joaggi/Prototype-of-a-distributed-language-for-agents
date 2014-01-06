identificador="[a-zA-Z]\w*"
servicio="(Videoconferencia|Mensajes)"
crear_agente='crear_agente "'+identificador+'"'
mover_agente='mover_agente "'+identificador+'"'
dispersar_agente='dispersar_agente "'+identificador+'"'
crear_comunidad='crear_comunidad "'+identificador+'"'
iniciar_servicio='iniciar_servicio "'+servicio+'"'
detener_servicio='detener_servicio "'+servicio+'"'
declaraciones=crear_agente+"|"+mover_agente+"|"+dispersar_agente+"|"+crear_comunidad+"|"+iniciar_servicio+"|"+detener_servicio

def getIdentificador():
	return identificador
	
def getServicio():
	return servicio
	
def getCrearAgente():
	return crear_agente
	
def getMoverAgente():
	return mover_agente

def getDispersarAgente():
	return dispersar_agente
	
def getCrearComunidad():
	return crear_comunidad
	
def getIniciarServicio():
	return iniciar_servicio
	
def getDetenerServicio():
	return detener_servicio
	
def getDeclaraciones():
	return declaraciones
