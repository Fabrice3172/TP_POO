class Entreprise:
    _nom : str
    _adresse : str
    _numero_siret : str
    
    def __init__(self, nom: str, adresse: str, siret: str) -> None:
        self._nom = nom
        self._adresse = adresse
        #self._numero_siret = siret
        if len(siret) == 14 : self._numero_siret = siret
        else: print("Entrer un SIRET sur 14 digit")
    
    @property
    def nom(self) -> str:
        return self._nom
    
    @nom.setter
    def nom(self, nom: str):
        self._nom = nom
        
    @property
    def adresse(self) -> str:
        return self._adresse
    
    @adresse.setter
    def adresse(self, adresse:str):
        self._adresse = adresse
        
    @property
    def numero_siret(self) -> str:
        return self._numero_siret
    
    @numero_siret.setter
    def numero_siret(self, numero:str):
        self._numero_siret = numero
    
    def __str__(self) -> str:
        return f"L'entreprise {self._nom}, ayant son siège social au {self._adresse}, possède le numero de SIRET : {self._numero_siret}"
    
e1 = Entreprise("MonEntreprise","Rue midi","12345678901234")

print(e1.nom)
print(e1.numero_siret)
e1.numero_siret= "12340987654321"
print(e1)   
    