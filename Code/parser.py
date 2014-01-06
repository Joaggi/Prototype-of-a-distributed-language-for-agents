import grammar as g
import re

def analizarSintaxis(all_tokens):
	p=re.compile(g.getDeclaraciones())
	i=1
	for token_list in all_tokens:
		if p.match(" ".join(token_list))==None:
			print "Error de sintaxis en la linea %d" %(i)
			return False
		else:
			print "Evaluar ejecucion del comando"
		i+=1
		
