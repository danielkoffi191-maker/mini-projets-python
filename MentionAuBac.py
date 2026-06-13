continuer = True

while continuer:
    try :
        moyenne = float(input("\nEntrez votre note moyenne au BAC : "))
        
        while not (0 <= moyenne <= 20):
            print("\nLa note est érronée\nEntrez une note valide ! ")
            moyenne = float(input("\nEntrez votre note moyenne au BAC : "))
            
        print()
        if moyenne >= 18:
            print("Vous obtenez les FELICITATIONS DU JURY !!\n")
        elif moyenne >= 16:
            print("Votre mention est : TRES BIEN\n")
        elif moyenne >= 14:
            print("Votre mention est : BIEN\n")
        elif moyenne >= 12:
            print("Votre mention est : ASSEZ BIEN\n")
        else:
            print("Désolé, vous n'avez pas de mention\n")
        
        reponse = input("Voulez-vous entrer une autre note ? (oui/non) : ").lower()
        if reponse not in ["oui", "yes", "yep", "wai", "ouais"]:
            continuer = False
            print("\nAu revoir !\n")
    except ValueError:
        print("\nErreur : Veuillez entrer un nombre valide !")