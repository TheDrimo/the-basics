# /usr/bin/env python3

import sys

if len(sys.argv) != 2 :
        print("erreur.")
        exit()

argument = sys.argv[1]

if ("AM" not in argument)&("PM" not in argument):
        print("erreur.")
        exit()

heure = ""
minute = ""
separateur = False
postmeridien=True

for i in argument :
        if i == ":" :
                separateur=True
        elif i=="A" :
                postmeridien=False
                break
        elif i=="P":
                break
        elif i==" ":
                continue
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

if ((heure<0) or (12<heure) or (minute<0) or (59<minute)) :
        print("erreur.")
        exit()

if postmeridien:
        if heure!=12 :
                heure += 12
else :
        if heure==12:
                heure=0

res = ""
if heure < 10 :
        res = "0"
res += str(heure)+":"
                
if minute<10 :
        res+="0"
res += str(minute)  
        
print(res)
