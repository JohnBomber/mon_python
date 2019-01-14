def string_float():
    """
    return print x
    :param x: int or float
    
    """
    x = input("un chiffre svp ")
    try:        
        x = float(x)
        print(x)
    except ValueError:
        print("Merci de saisir un chiffre")

    
