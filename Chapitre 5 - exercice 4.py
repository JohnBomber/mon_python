me = {
    "height": "6",
    "fav_color": "red",
    "fav_author": "Orwell"
}

n = input("what would you like to know ? (height, fav_color, fav_author ")
if n in me:
    x = me[n]
    print(x)
else:
    print(me)
