
# usr/bin/env python3

import sys

if len(sys.argv) == 1 :
        print("erreur.")
        exit()

try :
        for i in sys.argv[1:]:
                if int(i) != float(i):
                        print("erreur.")
                        exit()
except :
        print("erreur.")
        exit()

liste_entiers = [int(i) for i in sys.argv[1:]]

for i in range(0, len(liste_entiers)-1):
	if liste_entiers[i] > liste_entiers[i+1]:
		print("Pas triée !")
		exit()
print("Triée !")
