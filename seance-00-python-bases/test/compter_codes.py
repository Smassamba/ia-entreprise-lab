import csv                                  # module standard : évite d'écrire le découpage à la main

def compter_codes(chemin):                  # fonction : on pourra la réutiliser sur d'autres fichiers
    compteur = {}                           # dictionnaire vide : code -> nombre de requêtes
    with open(chemin, newline="", encoding="utf-8") as f:   # 'with' garantit la fermeture du fichier
        lecteur = csv.DictReader(f)         # accès par nom de colonne, plus lisible que par numéro
        for ligne in lecteur:               # une itération par requête
            code = ligne["code"]            # texte, par exemple "200" (jamais un entier)
            if code in compteur:            # clé déjà vue ?
                compteur[code] += 1         # oui : on ajoute 1 (raccourci de compteur[code] = compteur[code] + 1)
            else:
                compteur[code] = 1          # non : on crée la clé avec la valeur 1
    return compteur                         # on renvoie le résultat au lieu de l'afficher : plus réutilisable

resultat = compter_codes("access.csv")      # appel de la fonction
for code in sorted(resultat):               # sorted() trie les clés pour un affichage stable
    print(code, ":", resultat[code])
