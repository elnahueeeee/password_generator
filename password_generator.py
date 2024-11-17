import random

### characteres ###
characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# placeholder
password = ""
while True:
    languaje = input("select languaje(Spanish or English):")
    if languaje == "Spanish" or languaje == "English":
        ### bucle principal ###
        while languaje == "Spanish":
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
        
        while languaje == "English":
            ### length of the password ###
            print("enter the length of your password(advice, at least 6):")
            long = int(input())
            
            ### password creation ###
            for i in range(long):
                password += random.choice(characters)
            
            ### your password ###
            print("")
            print("this is your password:", password)
            print("")
    else:
        print("sintax error: try again")
        continue
