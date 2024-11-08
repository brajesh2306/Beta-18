from flask import request, jsonify
from utils.excel_reader import read_excel
from utils.sql_reader import fetch_sql_data
from models import FoodConsumption, Inventory
def init_routes(app, mysql):

    @app.route('/upload_excel', methods=['POST'])
    def upload_excel():
        if 'file' not in request.files:
            return jsonify({"error": "No file part"})
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"})
        
        data = read_excel(file)
        return jsonify({"message": "Data uploaded successfully", "data": data})

    @app.route('/get_sql_data', methods=['GET'])
    def get_sql_data():
        food_data = fetch_sql_data(mysql)
        return jsonify({"data": food_data})

