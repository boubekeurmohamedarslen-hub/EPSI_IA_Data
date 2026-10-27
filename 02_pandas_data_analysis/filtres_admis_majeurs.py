import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Nom": ["Ali", "Sara", "Yacine", "Lina"],
    "Age": [20, 2, 6, 23],
    "Note": [14, 8, 16, 11]
}
x = pd.DataFrame(data)
print(x)

print('moyenne age:',x["Age"].mean())

print('moyenne note:',x["Note"].mean())

print('maximum note:',x["Note"].max())
admis = x[x["Note"] >= 10]
non_admis = x[x["Note"] < 10]
print("Étudiants admis :")
print(admis)
print(non_admis)

majeur = x[x["Age"] >= 18]
print('majeur:',majeur)
resultat = x[(x["Age"] >= 18) | (x["Note"] >= 14)]

print(resultat)