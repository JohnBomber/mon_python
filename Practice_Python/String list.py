x = input("Give a word ")
word = list(x)
b = len(x)
reverse = []
i = 0
j = 0
palindrome = False

while i < b:
    c = b - i -1
    reverse.append(word[c])
    i += 1

print(word)
print(reverse)

while j < b:
    if word[j] == reverse[j]:
        palindrome = True
        j += 1
        continue
    else:
        palindrome = False
        break
if palindrome == True:
    print("Palindrome !")
else:
    print("Pas un palindrome")



# Autre méthode
wrd=input("Please enter a word")
wrd=str(wrd)
rvs=wrd[::-1]
print(rvs)
if wrd == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")

#Autre méthode
def reverse(word):
	x = ''
	for i in range(len(word)):
		x += word[len(word)-1-i]
		return x

word = input('give me a word:\n')
x = reverse(word)
if x == word:
    print('This is a Palindrome')
else:
    print('This is NOT a Palindrome')
