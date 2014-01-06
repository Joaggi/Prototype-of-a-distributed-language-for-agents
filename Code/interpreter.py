import lexer as l
import parser as p
import sys as s

tokens=l.analizarEntrada(s.argv[1])
if tokens!=None:
	p.analizarSintaxis(tokens)
