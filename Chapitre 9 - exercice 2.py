import os
x = input("comment ça va mon lapin ? ")
file_path = os.path.join("C:\\","Users","yannt","Desktop","PYTHON","monlapin.txt")
with open(file_path, "w") as fff:
    fff.write(x)
