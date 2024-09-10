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
    def somme(liste) -> float:
        s =0
        for cpt in liste:
            s += cpt._solde  
        return s  
            
l =  List(CompteBancaire) 
e1 = Client("nom", "prenom","adresse", "1234567890123455")
e2 = Client("nom", "prenom","adresse", "1234567890123455")

c1 = CompteBancaire("2024-01-01", e1, 100000)
c2 = CompteBancaire("2024-01-01", e2, 100000)

l.append(c1)
l.append(c2)

if c1.__eq__(c2):
    print("Les soldes des comptes bancaires sont égaux")
else:
    print("Les soldes des comptes bancaires sont différents")

ss= CompteBancaire.somme(l)
print("Somme des comptes bancaires : {ss}")

