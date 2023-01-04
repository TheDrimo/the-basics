# /usr/bin/env python3

import sys

if len(sys.argv) != 2 :
        print("erreur.")
        exit()

argument = sys.argv[1]

try :
        nombre = int(argument)
except :
        print("erreur.")
        exit()

if (nombre <= 0) :
        print("erreur.")
        exit()

if (nombre != float(argument)) :
	print("erreur.")
	exit()

res=nombre**0.5

if int(res) == res :
	res = int(res)

print(res)
