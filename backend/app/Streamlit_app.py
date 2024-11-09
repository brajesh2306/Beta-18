import streamlit as st
import pickle
import pandas as pd

# Load the model from the pickle file
with open('food_wastage_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Set page title and layout
st.set_page_config(page_title="Food Wastage Preventation", layout="centered")

# Title
st.title("Food Wastage Prediction System")
st.markdown("""
This application predicts the amount of food wastage based on meal details.
Please provide the following details to make a prediction.
""")

# Create a container for the input form
with st.form(key="input_form"):
    st.subheader("Enter Meal Details")

    # Collect input from the user using form fields
    day_of_week = st.selectbox("Day of the Week", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
    breakfast_dish = st.selectbox("Breakfast Dish",['Dosa', 'Baingan Bharta', 'Idli', 'Paneer Butter Masala', 'Rajma',
       'Pav Bhaji', 'Kheer', 'Dal Tadka', 'Aloo Gobi', 'Roti', 'Naan',
       'Chole', 'Paratha', 'Gulab Jamun', 'Jalebi'])
    dish1_name = st.selectbox("Dish 1 Name (e.g., Dal)",['Pav Bhaji', 'Idli', 'Kheer', 'Aloo Gobi', 'Naan', 'Gulab Jamun',
       'Roti', 'Dosa', 'Rajma', 'Dal Tadka', 'Baingan Bharta', 'Jalebi',
       'Paneer Butter Masala', 'Paratha', 'Chole'])
    dish2_name = st.selectbox("Dish 2 Name (e.g., Rice)",['Naan', 'Kheer', 'Gulab Jamun', 'Rajma', 'Pav Bhaji', 'Roti',
       'Paneer Butter Masala', 'Chole', 'Idli', 'Paratha', 'Dosa',
       'Jalebi', 'Dal Tadka', 'Baingan Bharta', 'Aloo Gobi'])
    dish3_name = st.selectbox("Dish 3 Name (e.g., Salad)",['Naan', 'Paneer Butter Masala', 'Paratha', 'Idli', 'Dosa', 'Rajma',
       'Roti', 'Kheer', 'Gulab Jamun', 'Dal Tadka', 'Aloo Gobi', 'Chole',
       'Jalebi', 'Baingan Bharta', 'Pav Bhaji'])
    staples1 = st.selectbox("Staple (e.g., Bread)",['Dal Tadka', 'Chole', 'Baingan Bharta', 'Jalebi', 'Naan', 'Rajma',
       'Pav Bhaji', 'Roti', 'Aloo Gobi', 'Dosa', 'Idli', 'Paratha',
       'Gulab Jamun', 'Kheer', 'Paneer Butter Masala'])
    dessert = st.selectbox("Dessert (e.g., Ice Cream)",['Chole', 'Dosa', 'Roti', 'Naan', 'Aloo Gobi', 'Baingan Bharta',
       'Dal Tadka', 'Rajma', 'Idli', 'Jalebi', 'Pav Bhaji', 'Kheer',
       'Paratha', 'Paneer Butter Masala', 'Gulab Jamun'])
    expected_diners = st.number_input("Expected Diners", min_value=0, step=1, value=100)
    meal_type = st.selectbox("Meal Type", ["Lunch", "Dinner","Breakfast"])

    # Submit button
    submit_button = st.form_submit_button("Predict Food Wastage")

# If the form is submitted, make predictions
if submit_button:
    # Collect all the input values into a dictionary
    input_values = {
        'Day of Week': day_of_week,
        'Breakfast Dish': breakfast_dish,
        'Dish1_Name': dish1_name,
        'Dish2_Name': dish2_name,
        'Dish3_Name': dish3_name,
        'Staples1': staples1,
        'Dessert': dessert,
        'Expected Diners': expected_diners,
        'Meal Type': meal_type
    }
    
    # Convert the input data into a DataFrame
    input_df = pd.DataFrame([input_values])

    # Make prediction using the model
    prediction = model.predict(input_df)
    
    # Display the result with a personalized message
    st.subheader("Prediction Results")
    st.write(f"Predicted Output: **{prediction[0]}**")

    # Display extra information about the prediction
    st.markdown("""
    - **Day of the Week:** The day of the week plays a key role in determining food consumption patterns.
    - **Expected Diners:** Adjust the number of diners for better predictions.
    - **Meal Type:** Lunch and Dinner have different consumption rates.
    """)

# # Add some styling to make the app look better
# st.markdown("""
#     <style>
#         .stTextInput>div>div>input {
#             background-color: #f0f0f5;
#             font-size: 16px;
#         }
#         .stButton>button {
#             background-color: #4CAF50;
#             color: white;
#             font-size: 16px;
#             border-radius: 5px;
#         }
#         .stButton>button:hover {
#             background-color: #45a049;
#         }
#         .stSelectbox>div>div>input {
#             background-color: #f0f0f5;
#             font-size: 16px;
#         }
#         .stForm {
#             background-color: #fafafa;
#             padding: 20px;
#             border-radius: 10px;
#         }
#         .stFormSubmitButton {
#             background-color: #0073e6;
#             color: white;
#             border-radius: 5px;
#         }
#         .stFormSubmitButton:hover {
#             background-color: #005bb5;
#         }
#     </style>
# """, unsafe_allow_html=True)

