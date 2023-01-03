# /usr/bin/env python3

import sys

if len(sys.argv) != 2 :
	print("erreur.")
	exit()

chaine = sys.argv[1]

if chaine.isnumeric():
	print("erreur.")
	exit()
else :
	print(len(chaine))
