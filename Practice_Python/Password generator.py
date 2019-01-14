'''
import random

def letter():
    x = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    y = random.randint(1,2)
    if y == 1:
        return x[number()].upper()
    else:
        return x[number()]
    
def number():
    return random.randint(0,9)

def special():
    x = " & ! ? : ; % * µ $ £".split()
    return x[number()]

def generate():
    x = int(input("how many character do you want in your password? "))
    z = []
    for i in range(0,x):
        y = random.randint(1,3)
        if y == 1:
            z.append(letter())
        elif y == 2:
            z.append(str(number()))
        else:
            z.append(special())
    return "".join(z)
'''


import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8
p =  "".join(random.sample(s,passlen ))
print(p)

import string
import random

def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))

print(pw_gen(int(input('How many characters in your password?'))))
