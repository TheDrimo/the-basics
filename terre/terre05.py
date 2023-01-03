# /usr/bin/env python3

import sys

if len(sys.argv) != 2 :
	print("Tu ne me la mettras pas à l'envers")
	exit()

argument = sys.argv[1]

"""if not argument.isnumeric() :
print("Tu ne me la mettras pas à l'envers")
exit()"""

try :
	nombre=int(argument)**2
except :
	print("Tu ne me la mettras pas à l'envers")
	exit()


if nombre%2==1 :
	print("impair")
else :
	print("pair")

