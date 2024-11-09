import joblib

def load_model():
    return joblib.load('path_to_model.pkl')

def predict_waste(input_data):
    model = load_model()
    prediction = model.predict(input_data)
    return prediction
