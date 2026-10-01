notes = [12, 15, 9, 17, 14]

for note in notes:
    if note >= 10:
        print(note, "validée")
    else:
        print(note, "non validée")
import pandas as pd

data = {
    "Nom": ["Ali", "Sara", "Yacine", "Lina", "Nora"],
    "Age": [22, 24, 21, 23, 25],
    "Note": [12, 16, 9, 14, 18]
}

df = pd.DataFrame(data)

print(df)
df["Note"].mean()
