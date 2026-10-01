import pandas as pd
import matplotlib.pyplot as plt

data = {
    "NOM":["Ali", "sarah", "Yacine", "Lina", "Imen"],
    "Age":[22, 24, 21, 23, 25],
    "Note":[12, 15, 16, 9, 7]
}
df = pd.DataFrame(data)
print(df)
df["Age"].mean()
print(df["Age"].mean())