import pandas as pd

etudiants = pd.DataFrame({
    "nom": ["yanis", "sarah", "amine", "lina", "samir", "nora"],
    "note": [8, 16, 12, 6, 14, 18]
})
def commentaire(note):
    if note >= 15:
        return'excellent'
    elif note >= 10:
        return 'admis'
    else:
        return 'non_admis'
etudiants['resultat'] = etudiants['note'].apply(commentaire)
print(etudiants)