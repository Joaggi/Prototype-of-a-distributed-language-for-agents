import lexer as l
import sys as s

tokens=l.analizarEntrada(s.argv[1])
if tokens!=None:
	print "Llamar a parser"
else:
	print "Terminando la compilacion"
