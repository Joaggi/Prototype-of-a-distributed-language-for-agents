import grammar as g
import re

def analizarEntrada(nombreArchivo):
	f = open(nombreArchivo, 'r')
	lines=list(f)
	all_tokens=[]
	i=1
	for line in lines:
		tokens=[]
		for token in line.rstrip().split(' '):
			if analizarToken(token)==False:
				print 'Error en "'+nombreArchivo+'", linea %d: El token "%s" es invalido' %(i,token)
				return None
			else:
				tokens.append(token)
		all_tokens.append(tokens)
		i+=1
	f.close()
	return all_tokens
	
def analizarToken(token):
	p=re.compile("("+g.getIdentificador()+'\Z|"'+g.getIdentificador()+'"\Z)')
	return p.match(token) is not None
