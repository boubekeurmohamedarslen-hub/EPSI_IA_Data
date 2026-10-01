import pandas as pd

employes = pd.DataFrame({
    "nom": ["adam", "lina", "yassine", "sara", "amine", "nora"],
    "age": [22, 27, 19, 31, 25, 23],
    "salaire": [1800, 2400, 1600, 2900, 2100, 1950],
    "anciennete": [1, 4, 1, 7, 3, 2]
})
def classement_sa(salaire):
    if salaire >= 2500:
        return 'eleve'
    elif salaire >= 2000:
        return 'moyen'
    else:
        return 'faible'
moy = employes['salaire'].mean()
max = employes['salaire'].max()
min = employes['salaire'].min()
age_moy = employes["salaire"].mean()
print(moy, max, min, age_moy)
ancien = employes.loc[
    (employes['anciennete'] >= 3 ) & (employes["salaire"] >= 2000),
    ['anciennete' , 'salaire' , 'nom']
]
print(ancien)
for i in range(len(employes)):
    nom = employes.loc[i, 'nom']
    age1 = employes.loc[i, 'age']
    salaire1 = employes.loc[i, 'salaire']
    anciennete1 = employes.loc[i, 'anciennete']
    niveau_salaire = classement_sa(salaire1)
    if age1 >= 25 and anciennete1 >=3:
        print(nom, age1, salaire1, niveau_salaire, "Profil expérimenté" )
    else :
        print(nom, age1, salaire1, niveau_salaire)   


    
   