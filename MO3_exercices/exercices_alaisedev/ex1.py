# Pour un logiciel de gestion rh d'une agence d'interim
# complétez la fonction suivante sui calcule le salaire journalier
# d'un intérimaire
# après 8 heures de travail, les heures sont majorées de 25%, après 11heures de 50%


def get_salaire_jour(nb_heures, salaire_horaire):
    if(nb_heures <= 8):
        return nb_heures * salaire_horaire
    if(nb_heures <= 11):
        return 8 * salaire_horaire + ((nb_heures - 8) * salaire_horaire) * 1.25
    else:
        return 8 * salaire_horaire + 11 * salaire_horaire * 1.25 + ((nb_heures - 11) * salaire_horaire) * salaire_horaire * 1.5



