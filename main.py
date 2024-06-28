import pandas as pd
from sklearn.model_selection import train_test_split
from lightgbm import LGBMRegressor
from sklearn.metrics import mean_squared_error, r2_score
import time
import joblib

# Load your dataset
df = pd.read_csv(r'C:\Users\mathe\Documents\Intel Industrial Training\26_06_simout\26_06_simout_combined.csv')
print(df.head())

base_features = ['start_x', 'start_y', 'end_x', 'end_y', 'distance', 'average_speed']
target = 'fee'
df = pd.get_dummies(df, columns=['vehicle_id'])
encoded_vehicle_id_columns = [col for col in df.columns if 'vehicle_id' in col]
features = base_features + encoded_vehicle_id_columns

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LGBMRegressor()

model.fit(X_train, y_train)

joblib.dump(model, "lgbm_model.sav")