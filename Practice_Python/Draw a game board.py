#méthode Yannou
ligne1_3 = "--- "
ligne2 = "   |"
base1_3 = " --- "
base2 = "|   |"

def quadrillage(x):
    if x == 1:
        print("""
     ---
    |   |
     ---
    """)
    else:
        premiere = base1_3 + ligne1_3 * (x-1)
        seconde = base2 + ligne2 * (x-1)
        ensemble = premiere + "\n" + seconde + "\n" + premiere
        ensemble2 = seconde + "\n" + premiere

    print(ensemble)
    for i in range(x-1):
        print(ensemble2)

quadrillage(int(input("combien par combien ? ")))

#correction
def drawboard(kamal):
    kamal = int(kamal)
    i = 0
    ho = " ---"
    ve = "|   "
    ho = ho * kamal
    ve = ve * (kamal+1)
    while i < kamal+1:
        print(ho)
        if not (i == kamal):
            print(ve)
        i += 1

