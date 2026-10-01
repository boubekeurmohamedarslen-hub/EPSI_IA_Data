import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Nom": ["Ali", "Sara", "Yacine", "Lina", "Nora"],
    "Age": [22, 24, 21, 23, 25],
    "Note": [12, 16, 9, 14, 18]
}

df = pd.DataFrame(data)

print(df)


plt.bar(df["Nom"], df["Note"])
plt.xlabel("Étudiants")
plt.ylabel("Notes")
plt.title("Notes des étudiants")
plt.show()