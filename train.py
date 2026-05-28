import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

df = pd.read_csv("data.csv")

X = df.drop("optimal_price", axis=1)
y = df["optimal_price"]

model = RandomForestRegressor()

model.fit(X, y)

pickle.dump(model, open("pricing_model.pkl", "wb"))

print("Model trained")