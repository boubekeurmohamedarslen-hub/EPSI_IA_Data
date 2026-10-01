import pandas as pd

classe = pd.DataFrame({
    "nom": ["amina", "karim", "sarah", "nabil", "ines", "mehdi"],
    "age": [20, 22, 19, 24, 18, 21],
    "note": [14, 8, 17, 11, 6, 15]
})
def evaluer_note(note):
    if note >= 15 :
        return 'excellent'
    elif note >= 10:
        return 'admis'
    else :
        return 'non admis'
moy = classe['note'].mean()
note_max = classe['note'].max()
note_min= classe['note'].min()
print(moy, note_max, note_min)
tri = classe.loc[
    (classe["note"] >= 10) & (classe['age'] >= 20),
    ['nom', 'note', 'age'],
]
print(tri)
for i in range(len(classe)):
    nom1 = classe.loc[i, 'nom']
    note1 = classe.loc[i, 'note']
    evaluation = evaluer_note(note1)
    print(nom1, evaluation )