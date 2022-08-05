#coding:utf-8
class Humain:
    humain_creer = 0 
    """ 
    Classe des êtres humains
    """
    def __init__(self,c_prenom,c_age):#self cible l'objet lui même
        print('création d\'un humain...')
        self.prenom = c_prenom
        self.age = c_age
        Humain.humain_creer +=1

print("Lancement du programme...")

h1 = Humain("manitra",23)
print("Humains existants: {}".format(Humain.humain_creer))
h2 = Humain("Luc",22)
print("Humains existants: {}".format(Humain.humain_creer))


 