from dataclasses import dataclass

@dataclass
class DatabaseConnection:
    type_db : str
    utilisateur : str
    mdp : str
    hote : str = "localhost"
    nb_instance : int = 0
    
    def __post_init__(self) :
        self.nb_instance += 1 # le compteur est static, on l'appel sur le nom de la classe
    
    @staticmethod
    def nbInstances(self) -> str : # static ne prend pas self en paramètre
        return f"La classe DatabaseConnection possède actuellement {self.nb_instance} instance(s)." # appel nb_instance en static
    
    @classmethod
    def cree_instance(cls):
        return cls("mariadb","root","1234","76.287.872.12")


objet = DatabaseConnection("maria","user","4321")
print(objet)

objet2 = DatabaseConnection.cree_instance()
print(objet2)

print(DatabaseConnection.nbInstances()) 