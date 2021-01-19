# Projet La poste
#
#
#QUESTION 1: enregistrer les noms des utilisateurs qui se sont connectés dans un fichier utilisateurs.txt
f = open('input/connexion.log','r')

liste_separee = []
for line in f:
    liste_separee.append(line.split(';')) #liste_separee: liste de listes (ip + pseudo + date et heure)
    
f.close()

utilisateurs = []

for i in liste_separee:
    utilisateurs.append(i[1]) #utilisateurs: on fait une liste avec le 2e élément de chaque liste


with open("utilisateurs.txt", "w") as filout:
    for i in utilisateurs:
        filout.write("{}\n".format(i)) #pour créer et remplir mon fichier utilisateurs.txt


#QUESTION 2 : id et ip des suspects hors heures autorisées
for i in liste_separee:
    a = i[2].split(' ') 
    heure = a[1].split(':')
    if int(heure[0])> 19 or int(heure[0])<8:
        print(i[0],i[1])


#QUESTION 3
#Donner la liste des ip dangereuses
fonction = open('input/warning.txt','r')
l= fonction.readlines() #liste des ip dangereuses
print(l)

#Donner les utilisateurs qui se sont connectés avec les ip suspectes
suspects = []

f = open('input/connexion.log','r')
line = f.readlines()
for i in line:
    for u in l:
        if i.split(";")[0]==u[:-1]:
            suspects.append(i.split(";")[1])

print(suspects)

f.close()

#Produire un fichier avec les utilisateurs suspects et le nombre de fois qu'ils se sont connectés aux adresses IP interdites
import collections
from collections import Counter

suspects_nb = Counter(suspects)
print(suspects_nb)


'''
#possibilité >> problème
def elt_nb(liste): #fonction qui donne une liste d'éléments/leur nb d'occurrences
    liste_sans_doublon = set(liste)
    liste_couple = []
    for elt in liste_sans_doublon:
        liste_couple.append(liste_sans_doublon.count(elt))
        return liste_couple #PB
            
print(elt_nb(suspects))

#possibilité >> incomplet
for o in suspects:
    print(o,";",suspects.count(o)) #PB: donne x fois le couple "elt/nb d'occurrences"
'''

with open("suspect.txt", "w") as filout:
    for i in suspects_nb:
        filout.write("{}\n".format(i)) #pour créer mon fichier suspect avec mes suspects/nombre de connexions

with open("suspect.txt", "r") as filin:
    for ligne in filin:
        print(ligne)
