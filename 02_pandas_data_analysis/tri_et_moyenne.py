import pandas as pd

df = pd.DataFrame({
    "nom": ["Arslen", "Samir", "Chakib", "Mohamed"],
    "note": [12, 8, 15, 10]
})
moy = df['note'].mean()
print(moy)
adm = df[df['note'] >= 10]
tri = df.sort_values('note', ascending=False)
print(tri)