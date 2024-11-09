import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import RandomForestRegressor
import joblib

df = pd.read_csv('final_df_with_output.csv')

selected_features = [
    'Day of Week', 'Breakfast Dish', 'Dish1_Name', 'Dish2_Name',
    'Staples1', 'Staples2', 'Dessert', 'Expected Diners', 'Meal Type'
]
target_columns = ['Dish1_Quantity_Made (kg)', 'Dish2_Quantity_Made (kg)', 'Staples1_Quantity_Made (kg)', 'Staples2_Quantity_Made (kg)']

X = df[selected_features]
y = df[target_columns]

categorical_features = X.select_dtypes(include=['object']).columns.tolist()
numerical_features = X.select_dtypes(include=['int64', 'float64']).columns.tolist()

numeric_transform = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

categorical_transform = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(transformers=[
    ('num', numeric_transform, numerical_features),
    ('cat', categorical_transform, categorical_features)
])

model = MultiOutputRegressor(RandomForestRegressor(random_state=42))

pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', model)
])

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipeline.fit(x_train, y_train)

joblib.dump(pipeline, 'food_waste_suggestion_model.pkl')
print("Model training complete and saved successfully!")


