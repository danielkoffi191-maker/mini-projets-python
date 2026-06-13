
while True :
    print()
    Temp = float(input("Entrez la température de l'eau :"))
    print()
    if Temp <0 :
        print("L'eau est à l'état Solide")
    elif Temp >100:
        print("L'eau est à l'état Gazeux")
    else :
        print("L'eau est à l'état Liquide")
        
    reponse = input("\nSouhaitez vous continuer ?")
    if reponse != "oui".strip().lower() :
        False
        print("\nAu revoir et à bientôt !")
        break 