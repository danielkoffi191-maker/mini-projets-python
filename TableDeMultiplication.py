print("\n", "="*23, "TABLE DE MULTIPLICATION", "="*23)

continuer = True
while continuer :
    try :
        print()
        nbre = int(input("Indiquez le nombre dont vous souhaitez obtenir la table de multiplication : "))
    
        print(f"\nVoici la table de multiplication de {nbre}")
        for i in range (1,11):
            print(f"{nbre} x {i} = {i*nbre}")
    
        reponse = input("\nVoulez vous continuez le programme avec un autre nombre ? (oui/non): ").lower()
        if reponse in ["oui", "wai", "yep", "yes"]:
            continuer = True
        else : 
            continuer = False
            print("\nAu revoir et à bientot !")
    except ValueError :
        print("Entrez un nombre valide ! ")