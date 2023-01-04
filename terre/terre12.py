# /usr/bin/env python3

import sys

if len(sys.argv) != 2 :
        print("erreur.")
        exit()

argument = sys.argv[1]

heure = ""
minute = ""
separateur = False

for i in argument :
	if i == ":" :
		separateur = True
	elif separateur :
		minute += i
	else :
		heure += i

try :
	heure = int(heure)
	minute = int(minute)
except :
	print("erreur.")
	exit()

if ((heure<0) or (23<heure) or (minute<0) or (59<minute)) :
	print("erreur.")
	exit()

if heure != 12 :
	heure = heure%12

res = ""
if heure < 10 :
	res = "0"
res += str(heure)+":"

if minute<10 :
	res+="0"
res += str(minute)+" PM"

print(res)
