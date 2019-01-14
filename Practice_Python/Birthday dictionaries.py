birthday = {"Ben":"02/07/1980",
            "Franck":"19/08/1985",
            "Yann":"16/04/1988"}

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
