import datetime
import json
import os


class Movie:
    _titre :str
    _date_sortie : str
    _resume : str
    
    MOVIE_DB = "movie.json"
    
    def __init__(self, titre, date_sortie, resume):
        self._titre = titre
        self._date_sortie = date_sortie
        self._resume = resume
        if not os.path.exists(self.MOVIE_DB):
            with open(self.MOVIE_DB, 'w') as fichier:
                json.dump([], fichier)

    def _lire_fichier(self):
        with open(self.MOVIE_DB, 'r') as fichier:
            return json.load(fichier)

    def _ecrire_fichier(self, donnees):
        with open(self.MOVIE_DB, 'w') as fichier:
            json.dump(donnees, fichier, indent=4)

    # Ajouter un film
    def ajouter_film(self, titre, date_sortie, resume):
        films = self._lire_fichier()
        titre = titre.title()
        film = {"titre": titre, "date_de_sortie": date_sortie, "description": resume}
        films.append(film)
        self._ecrire_fichier(films)
        print(f"Film {titre} ajouté avec succès")
        return film
    
    # Supprimer un film
    def supprimer_film(self, titre):
        films = self._lire_fichier()
        titre = titre.title()
        nouveaux_films = [film for film in films if film["titre"] != titre]
        self._ecrire_fichier(nouveaux_films)
        print(f"Film {titre} supprimé avec succès.")

    # Changement du titre, date de sortie ou description
    def changer_film(self, titre, date, resume):
        films = self._lire_fichier()
        titre = titre.title()
        for film in films:
            if film["titre"] == titre :
                titre2 = input("Entrez le nouveau titre du film : ")
                film["date_de_sortie"] = date
                film["description"] = resume
                film["titre"] = titre2.title()
            self._ecrire_fichier(films)
        print(f"Film {titre} modifié avec succès")
    
    #Lister les films
    def lister_films(self):
        films = self._lire_fichier()
        for film in films:
            print(f"{film["titre"]}  {film["date_de_sortie"]} {film["description"]}")
    
    #Lister les films par ordre croissant de date de sortie
    def lister_date(self):
        films = self._lire_fichier()
        dico = {}
        dico = sorted(films, key= lambda films : films["date_de_sortie"].split("/")[2])
        for film in dico:
            print(f"{film["titre"]}  {film["date_de_sortie"]} {film["description"]}")
    
    #Lister un film par son titre
    def lister_un_film(self, titre2):
        films = self._lire_fichier()
        for film in films:
            if (titre2 == film["titre"]):
                print(f"{film["titre"]}  {film["date_de_sortie"]} {film["description"]}")
            else:
                print(f"Film {titre2} non trouvé")
        
        
        
m = Movie("titre","date","description")

while(True):
    chiffre = input("Entrez le chiffre 1 pour commande create, le 2 pour commande read, le 3 pour commande update, le 4 pour commande delete et le 5 pour quitter : ")
    if chiffre == "5": break
    if chiffre == "1": 
        titre = input("donnez un titre de film : ")
        date = input("Entrez une date de sortie de ce film (format DD/MM/YYYY): ")
        tab = date.count("/")
        tab2 = date.split("/")
        if tab != 2 or not tab2[0].isdigit() or not tab2[1].isdigit() or not tab2[2].isdigit() :
            print("Erreur de date au format spécifié")
            break
        #if date.format({"DD/MM/YYYY"}) == False: break
        #date.strftime("%d/%m/%Y") : print("OK")
        #else: print("KO")
        resume = input("Entrez une courte description de ce film : ")
        m.ajouter_film(titre, date, resume)
        m.lister_films()
    if chiffre == "4":
        titre = input("Donnez le titre de film à supprimer :")
        m.supprimer_film(titre.title())
        m.lister_films()
    if chiffre == "3":
        titre = input("Donnez le titre du film à modifier :")
        #titre2 = input("Donnez le nouveau titre du film: ")
        date = input("Donnez la date modifiée (format DD/MM/YYYY) : ")
        desc = input("Donnez la nouvelle desciption du film: ")
        m.changer_film(titre.title(),date,desc)
        m.lister_films()
    if chiffre == "2":
        while(True):
            choix = input("Entrez 1 pour lister les films par ordre croissant de date de sortie, 2 pour afficher un film et 3 pour revenir au menu précédent: ")
            if choix == "1": 
                m.lister_date()
            if choix == "2": 
                titre2 = input("Entrez le titre du film à afficher : ")
                titre2 = titre2.title()
                m.lister_un_film(titre2)
            if choix == "3": 
                break
        
        
# m.ajouter_film("titre2","date2","description2")
# m.ajouter_film("titre3","date2","description2")
# m.ajouter_film("titre4","date2","description2")
# m.supprimer_film("Titre2")
# m.changer_film("Titre3","date3","description3")