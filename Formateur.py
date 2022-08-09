class Personne:
    def __init__(self):
        self.nom =" "
        self.prenom =" "
        self.age = 0
        self.ville =" "
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
class   Formateur(Personne):
    def __init__(self):
        super(Formateur, self).__init__()
        self.fonctionaire = ""
        self.tel = ""
        self.post = " "
    def saisie(self):
        Personne.saisie(self)
        self.fonctionaire = input("fonctionaire: ")
        self.tel = input("tel: ")
        self.post = input("port: ")
    def affichage(self):
        Personne.affichage(self)
        print("fonctionaire: ", self.fonctionaire)
        print("tel: ", self.tel)
        print("post: ", self.post)

este = Formateur()
este.saisie()
este.affichage()