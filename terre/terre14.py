# usr/bin/env python3

import sys

if len(sys.argv) != 4 :
	print("erreur.")
	exit()

try :
	for i in sys.argv[1:4]:
		if int(i) != float(i):
			print("erreur.")
			exit()
except :
	print("erreur.")
	exit()

liste_entiers = [int(i) for i in sys.argv[1:4]]
nb1, nb2, nb3 = liste_entiers

if (nb1==nb2 or nb1==nb3 or nb2==nb3):
	print("erreur.")
	exit()

for i in liste_entiers :
	score = 0
	for j in liste_entiers :
		if i > j :
			score += 1
		elif i < j :
			score -= 1
	if score==0:
		print(i)
