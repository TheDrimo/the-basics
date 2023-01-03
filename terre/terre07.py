# /usr/bin/env python3

import sys

if len(sys.argv) != 2:
	exit()

chaine = sys.argv[1][::-1]

print(chaine)
