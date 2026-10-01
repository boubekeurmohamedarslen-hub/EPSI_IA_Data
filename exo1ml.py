from sklearn.linear_model import LinearRegression
heures = [[1],[2],[3],[4],[5]]
notes = [8,10,12,14,16]
x = heures
y = notes
model = LinearRegression()
model.fit(x,y)
predicition = model.predict([[6]])
print(predicition)
