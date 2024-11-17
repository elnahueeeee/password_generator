import random

### characteres ###
characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# placeholder
password = ""

### bucle principal ###
while True:
    ### longitud de la contraseña ###
    print("introduzca la longitud de su contraseña(recomendacion, que tenga al menos 6):")
    long = int(input())

    ### creacion de la contraseña ###
    for i in range(long):
        password += random.choice(characters)

    ### inpresion de la contraseña ###
    print("")
    print("esta es tu contraseña:", password)
    print("")