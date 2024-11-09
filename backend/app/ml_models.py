import joblib

def load_model():
    return joblib.load('path_to_model.pkl')

def predict_waste(input_data):
    model = load_model()
    prediction = model.predict(input_data)
    return prediction

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Sample DataFrame creation (you should replace this with your actual DataFrame)
data = pd.read_csv('food_wastage_dataset_with_output.csv')

# Drop unnecessary columns
data.drop(columns=['Date', 'Weather'], inplace=True)

# Define feature set and target variable
X = data.drop(columns=['Output'])
y = data['Output']

# Identify numerical and categorical features
numerical_features = X.select_dtypes(include=['float64', 'int64']).columns.tolist()
categorical_features = X.select_dtypes(include=['object']).columns.tolist()

# Define the numeric and categorical transformers
numeric_transform = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', MinMaxScaler())
])

categorical_transform = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Create the preprocessor
preprocessor = ColumnTransformer(transformers=[
    ('num', numeric_transform, numerical_features),
    ('cat', categorical_transform, categorical_features)
])

# Define the model
model = RandomForestClassifier(random_state=42)

# Create the pipeline
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', model)
])

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit the pipeline
pipeline.fit(x_train, y_train)

# Make predictions and evaluate
y_pred = pipeline.predict(x_test)
print(classification_report(y_test, y_pred))
def input_data():
    # Prompt the user to input values for each feature
    input_values = {
        'Day of Week': input("Enter Day of Week (e.g., Monday): "),
        'Breakfast Dish': input("Enter Breakfast Dish (e.g., Eggs): "),
        'Dish1_Name': input("Enter Dish1 Name (e.g., Chicken Curry): "),
        'Dish2_Name': input("Enter Dish2 Name (e.g., Rice): "),
        'Dish3_Name': input("Enter Dish3 Name (e.g., Salad): "),
        'Staples1': input("Enter Staple (e.g., Bread): "),
        'Dessert': input("Enter Dessert (e.g., Ice Cream): "),
        'Expected Diners': float(input("Enter Expected Diners (e.g., 100): ")),
        'Meal Type': input("Enter Meal Type (e.g., Lunch or Dinner): ")
    }
    # Convert input into a DataFrame
    input_df = pd.DataFrame([input_values])
    
    # Make prediction using the pipeline
    prediction = pipeline.predict(input_df)
    print("Predicted Output:", prediction[0])

# Run the input function to test with custom inputs
input_data()