import os

fichier = "read.txt"
path_track = os.path.join("C:\\","Users","yannt","Desktop","PYTHON","Practice_Python",fichier)

#Methode 1
counter_dict = {}
with open(path_track) as f:
	line = f.readline()
	while line:
		line = line.strip()
		if line in counter_dict:
			counter_dict[line] += 1
		else:
			counter_dict[line] = 1
		line = f.readline()

print(counter_dict)

#Methode 2
counter_dict = {}
with open(path_track) as f:
	line = f.readline()
	while line:
		line = line[3:-26]
		if line in counter_dict:
			counter_dict[line] += 1
		else:
			counter_dict[line] = 1
		line = f.readline()

print(counter_dict)
