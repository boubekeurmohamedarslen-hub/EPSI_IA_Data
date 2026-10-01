import pandas as pd

x = pd.DataFrame({
    "nom": ["arslen", "chakib", "boub", "samir", "yanis"],
    "age": [25, 23, 18, 19, 21],
    "note": [12, 16, 9, 7, 14]
})
def evaluer_etudiant(note):
    if note >= 15 :
        return 'tres bien'
    elif note >= 10:
        return 'admis'
    else :
        return 'non admis'

moyenne= sum(x['note']) / len(x['note'])
print("Moyenne :", moyenne)
admis_majeur= x.loc[
    (x["note"] >= 10) & (x['age'] >= 18),
    ['nom', 'note', 'age']
]
print(admis_majeur)
for nom in x:
    print('nom', )



