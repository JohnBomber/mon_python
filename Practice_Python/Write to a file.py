import os
import csv
import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8
p =  "".join(random.sample(s,passlen ))

import string
import random

def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))

x = (pw_gen(int(input('How many characters in your password?'))))


#Pour fichier texte
"""
fichier = input("nom du fichier: ") + ".txt"
path_track = os.path.join("C:\\","Users","yannt","Desktop","PYTHON","Practice_Python",fichier)

with open(path_track,"w") as writetofile:
    writetofile.write(x)
"""

#pour csv

fichier = input("nom du fichier: ") + ".csv"
path_track = os.path.join("C:\\","Users","yannt","Desktop","PYTHON","Practice_Python",fichier)

with open(path_track,"w") as writetofile:
    writetocsv = csv.writer(writetofile)
    writetocsv.writerow(x)
