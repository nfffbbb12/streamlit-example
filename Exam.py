class Personne:
    def __init__(self):
        self.nom = " "
        self.prenom = " "
        self.age = 0
        self.ville = " "
    def saisie(self):
        self.nom = input("Nom: ")
        self.prenom = input("Prenom: ")
        self.age = input("Age: ")
        self.ville = input("Ville: ")
    def affichage(self):
        print("nom: ", self.nom)
        print("prenom: ", self.prenom)
        print("age: ", self.age)
        print("Il/Elle habite a :", self.ville)


costo = Personne()
costo.saisie()
costo.affichage()
