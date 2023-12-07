
# Ouvrir le fichier en mode lecture
with open('french_passwords_top20000.txt', 'r') as file:
    # Lire chaque ligne du fichier
    for line in file:
        # Récupérer le mot de la ligne correspondante en enlevant les espaces vides (si nécessaire)
        word = line.strip()
        
        # Utiliser le mot pour effectuer une action (dans cet exemple, afficher le mot)
        print(f"Mot de la ligne actuelle : {word}")
        
        # Ajoutez ici le code pour effectuer des opérations avec le mot de la ligne
        # Par exemple, vous pouvez ajouter le mot à une liste, le traiter d'une autre manière, etc.
