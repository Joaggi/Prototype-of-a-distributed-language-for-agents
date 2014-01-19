identificador="[a-zA-Z]\w*"
servicio="(Videoconferencia|Mensajes)"
iniciar_programa='iniciar_programa'
detener_programa='detener_programa'
crear_agente='crear_agente "'+identificador+'"'
eliminar_agente='eliminar_agente "'+identificador+'"'
recuperar_agente='recuperar_agente "'+identificador+'"'
dispersar_agente='dispersar_agente "'+identificador+'"'
crear_comunidad='crear_comunidad "'+identificador+'"'
iniciar_servicio='iniciar_servicio "'+servicio+'"'
detener_servicio='detener_servicio "'+servicio+'"'
declaraciones=detener_programa+"|"+iniciar_programa+"|"+crear_agente+"|"+eliminar_agente+"|"+recuperar_agente+"|"+dispersar_agente+"|"+crear_comunidad+"|"+iniciar_servicio+"|"+detener_servicio

def getIdentificador():
	return identificador
	
def getServicio():
	return servicio

def getIniciarPrograma():
    return iniciar_programa
    
def getDetenerPrograma():
    return detener_programa
	
def getCrearAgente():
	return crear_agente
	
def getEliminarAgente():
	return eliminar_agente

def getRecuperarAgente():
	return recuperar_agente

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
