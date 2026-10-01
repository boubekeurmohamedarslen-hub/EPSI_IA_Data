import pandas as pd

df = pd.DataFrame({
    "nom": ["Amine", "Sarah", "Yanis", "Lina", "Sofiane", "Emma"],
    "age": [19, 17, 22, 20, 18, 23],
    "note": [14, 16, 8, 12, 9, 18]
})
nombre_etudiant = len(df)
print('afficher le tableau:', df)
moy = df['note'].mean()
print('moyenne:', moy)
meilleure = df['note'].max()
mauvaise = df["note"].min()
print('meilleure note :', meilleure, 'mauvaise notes:', mauvaise)
best = df.loc[
    (df["note"] >= 10) & (df['age'] >= 18),
    ['nom', 'age']
]
print(best)
def evaluer_note(note):
    if note >= 15:
        return 'excellent'
    elif note >= 10:
        return 'admis'
    else :
        return 'nin admis'
df['resultat'] = df["note"].apply(evaluer_note)
print(df)  
best1 = df.loc[
    (df['note'] >= 10),
    ['nom', 'note'],
]
print(best1)
moy1 = best1['note'].mean()
print(moy1)
classement = best1.sort_values(by='note', ascending=False)
print(classement)
sup = best1.loc[
    (best1['note'] >= moy1),
    ['nom','note']
]

print(sup)
def ecarte_moy(note):
    x = note-moy
    return x
df['ecart'] = df['note'].apply(ecarte_moy)
print(df)
def position1(ecart):
    if ecart >= 0:
        return'au dessus'
    else :
        return 'en dessous'
df['position'] = df['ecart'].apply(position1)
print(df)
print(df.loc[df["note"] == meilleure, ["nom", "note"]])
sup = df.loc[df["ecart"] > 0, ["nom", "note", "ecart"]]
print(sup)