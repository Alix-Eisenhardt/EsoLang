#!/usr/bin/python

import sys

variables={}
name = ''
valueString = ''
valueNumber = 0
file = open(sys.argv[1], 'r').read()
i = 0

def val():
	return file[i]

def check(t):
	return val() == t
	
#This is so freaking stupid.
while i < len(file):
	#comments
	if(check('#')):
		i+=1
		while val() != '#':
			i+=1
	
	#declare
	if(check('d')):
		i+=1
		
		#string
		if(check('s')):
			i+=2
			while val() != ',':
				if (check('\\')):
					i+=1
				name += val()
				i+=1
			i+=1
			while val() != '.':
				valueString += val()
				i+=1
			variables[name] = valueString
			name = ''
			valueString = ''
		
		#integer (actually float is the same, I need to think hard about it)
		if(check('i') or check('f')):
			i+=2
			while val() != ',':
				if (check('\\')):
					i+=1
				name += val()
				i+=1
			i+=1
			while val() != '.':
				valueNumber *= 10
				valueNumber += int(val())
				i+=1
			variables[name] = valueNumber
			name = ''
			valueNumber = ''
		
		#boolean
		if(check('b')):
			i+=2
			while val() != ',':
				name += val()
				i+=1
			i+=1
			if(check('t') or check('T')):
				variables[name] = True
			else :
				variables[name] = False
			name = ''
			i+=2
	
	#output
	if(check('o')):
		i+=1
		
		#variable
		if(check('v')):
			i+=2
			while val() != '.':
				if (check('\\')):
					i+=1
				name += val()
				i+=1
			i+=1
			print variables[name]
			name = ''
		
		#print
		if(check('p')):
			i+=2
			while val() != '.':
				if (check('\\')):
					i+=1
				name += val()
				i+=1
			i+=1
			print(name)
			name = ''
			
	#loops
	if(check('l')):
		i+=1
		
		#if
		if(check('i')):
			i+=2
			while val() != '.':
				#todo
				i+=1
			
		#while
		if(check('w')):
			i+=2
			while val() != '.':
				#todo
				i+=1
		
	i += 1