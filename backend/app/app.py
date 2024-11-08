# backend/app/app.py
from flask import Flask
from flask_mysqldb import MySQL
from config import Config  # Import the Config class

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)  # Load the MySQL configuration

# Initialize MySQL connection
mysql = MySQL(app)

# Define a simple route
@app.route('/')
def index():
    return "Food Waste Reduction Platform API"

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
