#soit la liste d'élèves suivante
eleves = [
    "Thomas", "Bertrand", "Marie", "Etienne", "Jean", "Arnaud", "Bertrand", "Xavier", "Martin", "Jeanne",
    "David", "Rodolphe", "Genevieve", "Pierre", "Karim", "Ines", "Adrien", "Magalie", "Romaric", "Antoine",
    "Karim", "Ines", "Adrien", "Sofia", "Mehdi", "Clara", "Julien", "Amira", "Lucas", "Sarah", "Nicolas",
    "Leïla", "Thomas", "Amina", "Hugo", "Lina", "Yassine", "Emma", "Maxime", "Nawel", "Romain", "Chloé",
    "Antoine", "Samira", "Bastien", "Lila", "Quentin", "Jade", "Yanis", "Camille", "Alexandre", "Hana",
    "Théo", "Myriam", "Enzo", "Salma", "Victor", "Zoé", "Ayoub", "Manon"
]

# compte le nombre d'élèves
# en utilisant filter, crée un liste avec les élèves dont le prénom contient un a
# en utilisant filter, crée un liste avec les élèves dont le prénom contient plus de 7 caractère
# en utilisant filter, crée un liste avec les élèves dont le prénom fini par un d

long = len(eleves)
l1 = filter(lambda prenom : "a" in prenom, eleves)
l2 = filter(lambda prenom : len(prenom) > 7 , eleves)
l3 = filter(lambda prenom : prenom[-1] == "d" , eleves)

print(long)
print(list(l1))
print(list(l2))
print(list(l3))