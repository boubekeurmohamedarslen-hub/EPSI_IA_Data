import pandas as pd
import matplotlib.pyplot as plt
data = {
    'nom' : ['arslen', 'chakib', 'boub', 'samir'],
    'age' : [25, 23, 18, 19],
    'note' : [12, 15, 9, 7]
}
x = pd.DataFrame(data)
print(x)
print('moyenne gen:', x['note'].mean())
print('admis:', x[x['note'] >= 10])
resu = x[(x['age'] >= 18) & (x['note'] >= 10)]

print(resu)
