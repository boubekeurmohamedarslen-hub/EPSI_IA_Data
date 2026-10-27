from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
heures = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
notes = [8, 9, 10, 12, 13, 15, 16, 17, 18, 20]

x = heures
y = notes
x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)
model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print("Vraies notes :", y_test)
print("Prédictions :", y_pred)