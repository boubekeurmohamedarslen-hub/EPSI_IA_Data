def verifier_admission(note):
    if note >= 10:
        return "Admis"
    else:
        return "Refusé"

resultat = verifier_admission(9)
print(resultat)