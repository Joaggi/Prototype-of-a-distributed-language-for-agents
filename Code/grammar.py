identificador="[a-zA-Z]\w*"
servicio="(Videoconferencia|Mensajes)"
iniciar_programa='iniciar_programa'
detener_programa='detener_programa'
crear_agente='crear_agente "'+identificador+'"'
eliminar_agente='eliminar_agente "'+identificador+'"'
recuperar_agente='recuperar_agente "'+identificador+'"'
dispersar_agente='dispersar_agente "'+identificador+'"'
crear_comunidad='crear_comunidad "'+identificador+'"'
agregar_agente_comunidad='agregar_agente_comunidad "'+identificador+'" "'+identificador+'"'
agregar_servicio_comunidad='agregar_servicio_comunidad "'+identificador+'" "'+identificador+'"'
obtener_lista_agentes_comunidad='obtener_lista_agentes_comunidad "'+identificador+'"'
obtener_lista_agentes_host='obtener_lista_agentes_host "'+identificador+'"'
obtener_lista_movilidad_host='obtener_lista_movilidad_host "'+identificador+'"'
obtener_lista_racionalidad_host='obtener_lista_racionalidad_host "'+identificador+'"'
iniciar_servicio='iniciar_servicio "'+servicio+'"'
detener_servicio='detener_servicio "'+servicio+'"'
declaraciones=detener_programa+"|"+iniciar_programa+"|"+crear_agente+"|"+eliminar_agente+"|"+recuperar_agente+"|"+dispersar_agente+"|"+crear_comunidad+"|"+iniciar_servicio+"|"+detener_servicio+"|"+agregar_agente_comunidad+"|"+agregar_servicio_comunidad+"|"+obtener_lista_agentes_comunidad+"|"+obtener_lista_agentes_host+"|"+obtener_lista_movilidad_host+"|"+obtener_lista_racionalidad_host

def getIdentificador():
	return identificador
	
def getDeclaraciones():
	return declaraciones
