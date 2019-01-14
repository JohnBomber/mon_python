def Exercise1():
    name = input("What's your name ? ")
    age = input("How old are you ? ")
    copy = input("how many times want you this to be displayed ? ")
    try:
        age = int(age)
        copy = int(copy)
        age100 = 2018 + (100 - age)
        text = "Hey {}, you'll turn a 100 years old in {}\n".format(name,age100)
        print(copy * text)
    except ValueError:
        input("Please retry and give a number for your age and time displayed")
    

def Exercise1b():
    name = input("What's your name ? ")
    age = input("How old are you ? ")
    copy = input("how many times want you this to be displayed ? ")
    try:
        age = int(age)
        copy = int(copy)
        age100 = 2018 + (100 - age)
        text = "Hey {}, you'll turn a 100 years old in {}".format(name,age100)
        i = 0
        while i < copy:
            print(text)
            i += 1
    except ValueError:
        input("Please retry and give a number for your age and time displayed")
    
        
