#encoding: utf-8
import re, sys, lexer, grammar

p = re.compile(grammar.getIdentificador(),re.UNICODE)

f = open(sys.argv[1], 'r')
lines=list(f)
i=1
for line in lines:
	m=re.match(p,line)
	if m==None:
		print('Error de sintaxis en la linea %s: %s'%(i,line))
	i+=1
f.close()
