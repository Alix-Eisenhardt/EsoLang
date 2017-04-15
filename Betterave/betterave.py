#!/usr/bin/python

import sys

source = ""
index = -1
strings = []
variables = dict()
do = []

def parse():
    global source
    global index
    global strings
    global variables
    global do

    index += 1
    if index >= len(source):
        sys.exit(0)
    
    if source[index] == '$':
        print(strings[parse()], end='', flush=True)
    elif source[index] == '"':
        end = source.find("\"", index+1)
        if end == -1:
            print("Unmatched string!")
            sys.exit(1)
        else:
            strings.append(source[index+1:end])
            index = end
            return len(strings) - 1
    elif source[index].isalpha():
        if source[index].isupper():
            tmp = source[index] # Why does python evaluate dict key after parse()? :/
            variables[tmp] = parse()
            return variables[tmp]
        else:
            return variables.get(source[index].upper())
    elif source[index].isdigit():
        return int(source[index])
    elif source[index] == '+':
        return parse() + parse()
    elif source[index] == '-':
        return parse() - parse()
    elif source[index] == '*':
        return parse() * parse()
    elif source[index] == '/':
        return parse() / parse()
    elif source[index] == '%':
        return parse() % parse()
    elif source[index] == '=':
        return 1 if parse() == parse() else 0
    elif source[index] == '<':
        return 1 if parse() < parse() else 0
    elif source[index] == '>':
        return 1 if parse() > parse() else 0
    elif source[index] == '?':
        if parse() == 0:
            index = source.find("!", index)
            if index == -1:
                print("Unmatched if!")
                sys.exit(1)
    elif source[index] == '[':
        do.append(index)
    elif source[index] == '|':
        if len(do) == 0 or source.find("]", index) == -1:
            print("Unmatched do-while!")
            sys.exit(1)
        if parse() == 0:
            do.pop()
            index = source.find("]", index)
        else:
            index = do[-1]
    elif source[index] == '.':
        tmp = parse()
        print(tmp, end='', flush=True)
        return tmp
    elif source[index] == ',':
        tmp = parse()
        print(chr(tmp), end='', flush=True)
        return tmp
    elif source[index] == '~':
        index = source.find("~", index+1)
        if index == -1:
            print("Unmatched comment!")
            sys.exit(1)
    

if len(sys.argv) > 1:
    source = open(sys.argv[1], 'r').read()

while(index < len(source)):
    parse()
