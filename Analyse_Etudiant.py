import pandas as pd

x = pd.DataFrame({
    "nom": ["arslen", "chakib", "boub", "samir"],
    "age": [25, 23, 18, 19],
    "note": [12, 15, 9, 7]
})
bons_etudiants = x.loc[
    (x['age'] >= 20) & (x['note'] >= 12),
    ["nom", "age", "note"]
]

print(bons_etudiants)