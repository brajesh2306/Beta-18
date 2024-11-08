# backend/app/app.py
from flask import Flask
from flask_mysqldb import MySQL
from config import Config  # Import the Config class
from routes import init_routes

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)  # Load the MySQL configuration

# Initialize MySQL connection
mysql = MySQL(app)

# Initialize routes
init_routes(app, mysql)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
