import lexer as l
import parser as p
import sys as s

tokens=l.analizarEntrada(s.argv[1])
if tokens!=None:
	if p.analizarSintaxis(tokens)==False:
		print "\nLa ejecucion termino inesperadamente"
	else:
		print "\nLa ejecucion termino exitosamente"
else:
	print "\nLa ejecucion termino inesperadamente"
