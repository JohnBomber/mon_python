import statistics

base = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

y = 0
answer = True
compteur = 0

while answer:
    if len(base) > 2:
        compteur += 1
        z = int(statistics.mean(base))
        a = base.index(z)
        y = input("is it more, less or equal to : " + str(z) + " ? ")
        if y == "more":
            base = base [a:]
        elif y == "less":
            base = base[:a]
        elif y == "equal":
            print("the number was " + str(z))
            print("It took " + str(compteur) + " guesses")
            answer = False
            break
        else:
            print("wrong input")
            answer = False
            break
    else:
        for i in base:
            compteur += 1
            y = input("is it equal to : " + str(i) + " ? : yes or no ")
            if y == "yes":
                print("the number was " + str(i))
                print("It took " + str(compteur) + " guesses")
                answer = False
                break
