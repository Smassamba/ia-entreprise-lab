import csv

compteurs = {}

with open("alertes.csv", newline="", encoding="utf-8") as fichier:
    lecteur = csv.DictReader(fichier)
    for ligne in lecteur:
        niveau = ligne["niveau"]
        if niveau not in compteurs:
            compteurs[niveau] = 0
        compteurs[niveau] += 1

for niveau, total in compteurs.items():
    print(niveau, ":", total)
