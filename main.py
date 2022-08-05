# gestion d'erreur
ageUtilisateur = input("Quel âge as-tu?")

"""
premier cas
try:
    ageUtilisateur = int(ageUtilisateur)
    print('tu as', ageUtilisateur, "ans")
except:
    print("l'age entrer et incorrect!")
 """

# deuxiéme cas
"""
try:
    ageUtilisateur = int(ageUtilisateur)
except:
    print("l'age entrer et incorrect!")
else:#si l'except est sauter 
    print('tu as', ageUtilisateur, "ans")
finally: # ici ce finally s'execute toujours 
    print('Fin du programme...')
"""

"""
Gérer les excptions: try/except (+else,finally)

Types d'exceptions : ValueError
                    NameError
                    TypeError
                    ZeroDivisionError
                    OsError
                    AssertionError
"""
"""
nombre1 = 150
nombre = input('choisir le pour diviser 150= ')

try:
    nombre = int(nombre)
    print('le resultat de la division est {}'.format(nombre1/nombre))
except ZeroDivisionError:
    print('impossible de diviser avec zéro')
except ValueError:
    print('Vous devez entrer un nombre')
except:
    print('Valeur incorrecte')
else:
    print('Bravo tu as noté un nombre valide!')
finally: 
    print('Fin du programme...')"""

# utilisation d'une assertion

age = input('quel âge as-tu? ')
age = int(age)

assert age < 25 # on veut que âge soit inférieur à 25
#si on entre un nombre supérieur a 25 on a une AssertionError
