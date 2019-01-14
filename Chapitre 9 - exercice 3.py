import os
import csv

file = [
    ["Top Gun", "Risky Business", "Minority Report"],
    ["Titanic","The Revenant", "Inception"],
    ["Training Day", "Man on Fire", "Flight"]
       ]

file_path = os.path.join("C:\\","Users","yannt","Desktop","PYTHON","monlapin.csv")

with open(file_path, mode="w", newline='') as lapin:
    fichier = csv.writer(lapin, delimiter=",")
    for acteur in file:
        fichier.writerow(acteur)
