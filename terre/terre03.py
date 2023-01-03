# /usr/bin/env python3

import sys

arguments = sys.argv
if len(arguments)>1 :
	for a in arguments[1:] :
		print(a)
