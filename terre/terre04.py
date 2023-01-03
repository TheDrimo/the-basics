# /usr/bin/env python3

import string
import sys

alphabet = string.ascii_lowercase
res = ""
if len(sys.argv) != 2 :
	exit()
else :
	lettre = sys.argv[1]
affichage = False
if (len(lettre)!=1) or (lettre not in alphabet) :
	exit()
for i in alphabet :
	if lettre==i :
		affichage=True
	if affichage==True:
		res += i
print(res)
