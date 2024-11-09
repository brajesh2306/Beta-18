import joblib

def load_model():
    return joblib.load('path_to_model.pkl')

# def predict_waste(input_data):
#     model = load_model()
#     prediction = model.predict(input_data)
#     return prediction

# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_absolute_error, mean_squared_error
# import xgboost as xgb
# from statsmodels.tsa.statespace.sarimax import SARIMAX
# from prophet import Prophet
# from keras.models import Sequential
# from keras.layers import LSTM, Dense
# from keras.preprocessing.sequence import TimeseriesGenerator
# import matplotlib.pyplot as plt

# data = pd.read_csv('/mnt/data/food_wastage_dataset_with_output.csv')
# data['date'] = pd.to_datetime(data['date'])

# print(data.head())
# print(data.info())


# data['day_of_week'] = data['date'].dt.dayofweek
# data['month'] = data['date'].dt.month
# data['is_weekend'] = data['day_of_week'] >= 5


# train_size = int(len(data) * 0.8)
# train, test = data[:train_size], data[train_size:]

# X_train = train.drop(['date', 'food_demand'], axis=1)
# y_train = train['food_demand']
# X_test = test.drop(['date', 'food_demand'], axis=1)
# y_test = test['food_demand']

# sarima_model = SARIMAX(y_train, order=(1, 1, 1), seasonal_order=(1, 1, 1, 7)).fit(disp=False)
# sarima_pred = sarima_model.forecast(len(y_test))

# prophet_df = train[['date', 'food_demand']].rename(columns={'date': 'ds', 'food_demand': 'y'})
# prophet_model = Prophet()
# prophet_model.fit(prophet_df)
# future = prophet_model.make_future_dataframe(periods=len(test))
# prophet_pred = prophet_model.predict(future)['yhat'][-len(y_test):]

# xgb_model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100)
# xgb_model.fit(X_train, y_train)
# xgb_pred = xgb_model.predict(X_test)

# train_generator = TimeseriesGenerator(y_train.values, y_train.values, length=10, batch_size=1)
# test_generator = TimeseriesGenerator(y_test.values, y_test.values, length=10, batch_size=1)


# lstm_model = Sequential([
#     LSTM(50, activation='relu', input_shape=(10, 1)),
#     Dense(1)
# ])
# lstm_model.compile(optimizer='adam', loss='mse')
# lstm_model.fit(train_generator, epochs=5)
# lstm_pred = lstm_model.predict(test_generator)


# def evaluate_model(y_true, y_pred, model_name):
#     mae = mean_absolute_error(y_true, y_pred)
#     mse = mean_squared_error(y_true, y_pred)
#     print(f"{model_name} - MAE: {mae:.2f}, MSE: {mse:.2f}")
    
    
# evaluate_model(y_test, sarima_pred, 'SARIMA')
# evaluate_model(y_test, prophet_pred, 'Prophet')
# evaluate_model(y_test, xgb_pred, 'XGBoost')
# evaluate_model(y_test[10:], lstm_pred, 'LSTM')

# plt.figure(figsize=(14, 7))
# plt.plot(y_test.values, label='Actual')
# plt.plot(sarima_pred, label='SARIMA Prediction')
# plt.plot(prophet_pred.values, label='Prophet Prediction')
# plt.plot(xgb_pred, label='XGBoost Prediction')
# plt.plot(range(10, len(lstm_pred) + 10), lstm_pred, label='LSTM Prediction')
# plt.legend()
# plt.title('Model Comparison on Test Data')
# plt.show()

# New Model ------------>>>

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load the dataset
df = pd.read_csv('final_df_with_output.csv')

# Define selected input features and target columns
selected_features = [
    'Day of Week', 'Breakfast Dish', 'Dish1_Name', 'Dish2_Name',
    'Staples1', 'Staples2', 'Dessert', 'Expected Diners', 'Meal Type'
]
target_columns = ['Dish1_Quantity_Made (kg)', 'Dish2_Quantity_Made (kg)', 'Staples1_Quantity_Made (kg)', 'Staples2_Quantity_Made (kg)']

# Split the data into features (X) and targets (y)
X = df[selected_features]
y = df[target_columns]

# Preprocessing: Separate numerical and categorical features
categorical_features = X.select_dtypes(include=['object']).columns.tolist()
numerical_features = X.select_dtypes(include=['int64', 'float64']).columns.tolist()

# Define transformers
numeric_transform = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

categorical_transform = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Create preprocessor
preprocessor = ColumnTransformer(transformers=[
    ('num', numeric_transform, numerical_features),
    ('cat', categorical_transform, categorical_features)
])

# Multi-output regression model
model = MultiOutputRegressor(RandomForestRegressor(random_state=42))

# Create the pipeline
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', model)
])

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the pipeline
pipeline.fit(x_train, y_train)

# Save the model
joblib.dump(pipeline, 'food_waste_suggestion_model.pkl')
print("Model training complete and saved successfully!")


