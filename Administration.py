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
class Administration(Personne):
    def __init__(self):
        super(Administration, self).__init__()
        self.salair = " "
        self.heurs_travail = " "
        self.email = " "
    def saisie(self):
        Personne.saisie(self)
        self.salair = input("salaire :")
        self.heurs_travail = input("heure_de_travaille :")
        self.email = input("email :")
    def affichage(self):
        Personne.affichage(self)
        print("salaire: ", self.salair)
        print("heure_de_travaille : ", self.heurs_travail)
        print("email: ", self.email)

sio = Administration()
sio.saisie()
sio.affichage()