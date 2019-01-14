a = input("give any text to have it in reverse ")

# en 1 ligne
def reverseword(a):
    return ' '.join(a.split()[::-1])

# décomposer
def convert_to_list(a):
    b = a.split() #si split() prendra comme paramètre par défaut " "
    return b

#retourner v1
def reverse_list(a):
    y = a.split()[::-1] #retourner la liste
    return " ".join(y) #le raccorder en string séparé par des espaces

#retourner v2
def reverse(a):
    a = a.split()
    y = list(reversed(a))
    return " ".join(y)
