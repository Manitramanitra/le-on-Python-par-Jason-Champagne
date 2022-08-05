# coding:utf-8  
class Humain:
    humain_creer = 0 # ceci est une attribut de classe ceci est liée à la classe qui appartient a tous les classes
    lieu_habitation = "terre"
    """ 
    Classe des êtres humains
    """

    def __init__(self, c_prenom, c_age):  # mot clé 'self' cible l'objet lui même sur un intance
        print('création d\'un humain...')
        self.prenom = c_prenom
        self.age = c_age
        Humain.humain_creer += 1
    def parler(self,message):
        print("{} a dit: {} ".format(self.prenom,message))
     
    def changer_planete(cls,nouvelle_planete): # cls méthode de classe
        Humain.lieu_habitation = nouvelle_planete  
    changer_planete = classmethod(changer_planete)

    def definition():
        print("blablabla...")
    definition = staticmethod(definition)
print("Lancement du programme...")

h1 = Humain("manitra", 23)
print("Humains existants: {}".format(Humain.humain_creer)) 

print("Planéte ancien: {} ".format(Humain.lieu_habitation))

Humain.changer_planete("Mars")
print("Planéte actuelle: {} ".format(Humain.lieu_habitation))

Humain.definition()