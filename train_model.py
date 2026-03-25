import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Simulated route dataset with edges between cities
routes = pd.DataFrame({
    'start': ['Tiruvallur','Tiruvallur','Tanjore','Tanjore','Viluppuram','Viluppuram'],
    'end':   ['Tanjore','Viluppuram','Tiruchy','Viluppuram','Chennai','Chennai'],
    'crime_rate':[3,5,4,2,6,3],
    'lighting_score':[8,6,7,8,5,7],
    'crowd_density':[6,5,7,6,8,7]
})

# Safety score = higher is safer
routes['safety_score'] = (10 - routes['crime_rate']) + routes['lighting_score'] + routes['crowd_density']

# Train model
X = routes[['crime_rate','lighting_score','crowd_density']]
y = routes['safety_score']

model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X,y)

joblib.dump(model,'model.pkl')
routes.to_csv('routes.csv', index=False)
print("Model and route dataset created!")