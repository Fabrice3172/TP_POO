from typing import List
from client import Client
import datetime

class CompteBancaire:
    _date_creation : datetime
    _client : Client
    _solde : float
    
    def __init__(self, date : datetime, client:Client, solde: float) -> None:
        self._date_creation = date
        self._client = client
        self._solde = solde
        
    def __eq__(self, cpte) -> bool:
        if self._solde == cpte._solde : return True
        else : return False
    
    @staticmethod
    def somme(liste) -> float: # tu n'es pas sensé utiliser la méthode ceci, mais garder en mémoire les comptes bancaires car la classe
        s =0
        for cpt in liste:
            s += cpt._solde  
        return s  
            
l =  List(CompteBancaire) # c'est List du module typing pour le typage, pas list() qui transforme un élément en liste
e1 = Client("nom", "prenom","adresse", "123456789012345")
e2 = Client("nom", "prenom","adresse", "123456789012345")

c1 = CompteBancaire("2024-01-01", e1, 100000)
c2 = CompteBancaire("2024-01-01", e2, 100000)

l.append(c1)
l.append(c2)

if c1.__eq__(c2): # utilisation du __eq__ pour comparer les soldes avec le '=='
    print("Les soldes des comptes bancaires sont égaux")
else:
    print("Les soldes des comptes bancaires sont différents")

ss= CompteBancaire.somme(l)
print(f"Somme des comptes bancaires : {ss}") # n'oublie pas le 'f' devant la 'string' pour avoir un f-string

