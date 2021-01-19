'''
# Ouverture du fichier prenoms.txt
f = open('input/prenoms.txt', 'r')
liste_prenoms=[]

for line in f:
    liste_prenoms.append(line.strip()) #la fonction .strip() permet de retirer le '\n' dans la liste 


print(liste_prenoms)

# Fermeture du fichier prenoms.txt
f.close()
'''

# projet la poste
f = open('input/connexion.log','r')

liste_separee = []
for line in f:
    liste_separee.append(line.split(';')) #liste_separee: liste de listes (ip + pseudo + date  heure)
    
f.close()

utilisateurs = []

for i in liste_separee:
    utilisateurs.append(i[1]) #utilisateurs: on fait une liste avec le 2e élément de chaque liste


with open("utilisateurs.txt", "w") as filout:
    for i in utilisateurs:
        filout.write("{}\n".format(i)) #pour créer et remplir mon fichier utilisateurs.txt

'''
with open("utilisateurs.txt", "r") as filin:
    for ligne in filin:
        print(ligne) #juste pour vérifier que ça a marché
'''

for i in liste_separee:
    a = i[2].split(' ') 
    heure = a[1].split(':')
    if int(heure[0])> 19 or int(heure[0])<8:
        print(i[0],i[1])

