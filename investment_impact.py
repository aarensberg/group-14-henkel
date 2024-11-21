import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

brico_sellin = pd.read_csv("bricomarche_sell_in_22_23.csv")
brico_visites = pd.read_csv("bricomarche_visites_annuelles_22_23.csv")

data = pd.merge(brico_sellin, brico_visites, on='Code du Point de Vente')
data['Investissements_Total'] = data['BUDGET\nACCORD\nHT €'].astype(float)  

X = data[['Investissements_Total', 'Total visites annuelles\n2023']]
y = data['Total\nannuel\n2023']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("R²:", r2_score(y_test, y_pred))
print("RMSE:", mean_squared_error(y_test, y_pred, squared=False))

coefficients = pd.DataFrame({'Variable': X.columns, 'Coefficient': model.coef_})
print(coefficients)