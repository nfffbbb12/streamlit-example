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
class   Etudiant(Personne):
    def __init__(self):
        super(Etudiant, self).__init__()
        self.universite = ""
        self.niveau = ""
        self.filler = ""
    def saisie(self):
        Personne.saisie(self)
        self.universite = input("universite: ")
        self.niveau = input("niveau: ")
        self.filler = input("filler: ")
    def affichage(self):
        Personne.affichage(self)
        print("universite: ", self.universite)
        print("niveau: ", self.niveau)
        print("filler: ", self.filler)

dio = Etudiant()
dio.saisie()
dio.affichage()