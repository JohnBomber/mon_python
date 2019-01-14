import os

premier = "premier.txt"
path_track1 = os.path.join("C:\\","Users","yannt","Desktop","PYTHON","Practice_Python",premier)
happy = "happy.txt"
path_track2 = os.path.join("C:\\","Users","yannt","Desktop","PYTHON","Practice_Python",happy)

premier_liste = []
happy_liste = []
with open(path_track1) as f:
        line = f.readline()
        while line:
                line = int(line)
                if line in premier_liste:
                        continue
                else:
                        premier_liste.append(line)
                line = f.readline()


with open(path_track2) as f:
        line = f.readline()
        while line:
                line = int(line)
                if line in happy_liste:
                        continue
                else:
                        happy_liste.append(line)
                line = f.readline()

overlap = []
overlap = [j for i in premier_liste for j in happy_liste if j == i and j not in overlap]

print(overlap)
                
# Solution compacte
"""


def filetolistofints(filename):
	list_to_return = []
	with open(filename) as f:
		line = f.readline()
		while line:
			list_to_return.append(int(line))
			line = f.readline()
	return list_to_return

primeslist = filetolistofints('primenumbers.txt')
happieslist = filetolistofints('happynumbers.txt')

overlaplist = [elem for elem in primeslist if elem in happieslist]
print(overlaplist)


"""
