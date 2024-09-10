from itertools import count


class Client:
    _nom : str
    _prenom : str
    _adresse : str
    _nir : str
    
    @property
    def nir(self):
        return self._nir
    
    @nir.setter
    def nir(self, valeur : str):
        self._nir = valeur
    
    def __init__(self, nom, prenom, adresse, valeur) -> None:
        self._nom = nom
        self._prenom = prenom
        self._adresse = adresse
        #self._nir = valeur
        #Controle sur NIR
        if len(valeur) != 15 : 
            return "Entrer un nir sur 15 chiffres"
        else: self._nir = valeur
        
    def __str__(self) -> str:
        return f" {self._nom} {self._prenom} {self._adresse} {self._nir}"
    
c = Client("nom", "prenom","adresse", "123456789012345")
print(c) 
    
    