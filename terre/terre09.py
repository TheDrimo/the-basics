# /usr/bin/env python3

import sys

if len(sys.argv) != 3 :
        print("erreur.")
        exit()

argument1, argument2 = sys.argv[1], sys.argv[2]

try :
        nombre1, nombre2 =int(argument1), int(argument2)
except :
        print("erreur.")
        exit()

if (nombre2 < 0) :
        print("erreur.")
        exit()

res = 1
if nombre2 == 0:
	print(1)
else :
	for i in range(0, nombre2) :
		res *= nombre1
	print(res)
