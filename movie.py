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
        return film
    
    # Supprimer un film
    def supprimer_film(self, titre):
        films = self._lire_fichier()
        nouveaux_films = [film for film in films if film["titre"] != titre]
        self._ecrire_fichier(nouveaux_films)
        return f"Film {titre} supprimé avec succès."

    # Changement du titre, date de sortie ou description
    def changer_film(self, titre, date, resume):
        films = self._lire_fichier()
        for film in films:
            if film["titre"] == titre :
                film["date_de_sortie"] = date
                film["description"] = resume
            self._ecrire_fichier(films)
            

m = Movie("titre","date","description")
m.ajouter_film("titre2","date2","description2")
m.ajouter_film("titre3","date2","description2")
m.ajouter_film("titre4","date2","description2")
print(m.supprimer_film("Titre2"))
m.changer_film("Titre3","date3","description3")