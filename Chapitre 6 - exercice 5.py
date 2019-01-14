liste = ["The","fox","jumped","over","the","fence","."]
liste.pop()
phrase = " ".join(liste)+"."
print(phrase)

#Ou autre méthode
fox = ["The", "fox", "jumped", "over", "the", "fence", "."]
fox = " ".join(fox)
fox = fox[0: -2] + "."
print(fox)
