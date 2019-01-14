import os
import csv
path_track = os.path.join("C:\\","Users","yannt","Desktop","Téléphone 2018.csv")
with open(path_track,"r") as test123:
    r = csv.reader(test123, delimiter=";")
    for row in r:
        print(row)
