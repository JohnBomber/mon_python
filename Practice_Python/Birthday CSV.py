import os
import csv

fichier = "birthday.csv"
fichier2 = "birthday - virgule.csv"
path_track = os.path.join("C:\\","Users","yannt","Desktop","PYTHON","Practice_Python",fichier)
path_track2 = os.path.join("C:\\","Users","yannt","Desktop","PYTHON","Practice_Python",fichier2)

birthday = {}
list_birthday = []

with open(path_track2, "r") as f:
    w = csv.reader(f)
    for row in w:
        x = ",".join(row) #pour transformer mes données stockées en csv avec séparateur = "," en string
        x = x.split(",") #transformer mes strings en liste (texte séparé par une ","
        birthday[x[0]] = x[1] #rajouter les éléments dans mon dictionnaire birthday


"""
with open(path_track, "r") as f:
    w = csv.reader(f)
    for row in w:
        x = "\t".join(row) #pour transformer mes données stockées en csv avec séparateur de tab = \t en string
        x = x.split("\t") #transformer mes strings en liste (texte séparé par une tabulation = \t
        birthday[x[0]] = x[1] #rajouter les éléments dans mon dictionnaire birthday
"""

print("Welcome to the birthday dictionary. We know the birthdays of:")
for name in birthday:
    print(name)
name = input("Who's birthday do you want to look up?\n")

if name  in birthday:
    print("{}'s birthday is {}".format(name, birthday[name]))
else:
    print("Sadly, we don't have {}'s birthday.".format(name))
    date = input("What is {}'s birthdate ?, please type dd/mm/yyyy\n".format(name))
    birthday[name] = date
    print("{}'s birthday is {}".format(name, birthday[name]))

#transformer mon dictionnaire birthday en liste de liste (2 éléments dans chaque liste correspondant au key-value)
for name in birthday:
    x = birthday[name]
    list_birthday.append([name,x])

with open(path_track2,"w+",newline="") as f:
    w = csv.writer(f, delimiter=",")
    for liste in list_birthday:
        w.writerow(liste)
