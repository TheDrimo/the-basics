# /usr/bin/env python3

import sys

if len(sys.argv) != 3 :
        print("Tu ne me la mettras pas à l'envers")
        exit()

argument1, argument2 = sys.argv[1], sys.argv[2]

try :                           
        nombre1, nombre2 =int(argument1), int(argument2)            
except :
        print("Tu ne me la mettras pas à l'envers")
        exit()

if (nombre1 < nombre2) or (nombre2 <= 0) :
	print("erreur.")
	exit()

resultat = nombre1//nombre2
reste = nombre1%nombre2

print("résultat: ", resultat)
print("reste: ", reste)
