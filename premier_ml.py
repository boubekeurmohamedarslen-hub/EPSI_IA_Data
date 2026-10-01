heures = [[1], [2], [3], [4], [5]]

notes = [8, 10, 12, 14, 16]
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(heures, notes)
prediction = model.predict([[6]])
print(prediction)