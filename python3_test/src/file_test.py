#!/usr/bin/evn python3

import os
import tempfile

fh = None
try:
    fh = tempfile.NamedTemporaryFile('w')
    print(fh.name)
#    fh = open('a.txt', "w", encoding="utf8")
    a = os.listdir('./')
    for i in a:
        fh.write(i+'\n')
except EnvironmentError as err:
        print(err)
finally:
    if fh is not None:
        fh.close()
        
        


