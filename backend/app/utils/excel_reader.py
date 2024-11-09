# backend/app/utils/excel_reader.py
import pandas as pd

def read_excel(file):
    try:
        df = pd.read_excel(file)
        data = []
        for index, row in df.iterrows():
            data.append({
                "food_item": row['food_item'],
                "quantity_consumed": row['quantity_consumed'],
                "quantity_wasted": row['quantity_wasted'],
                "date": row['date']
            })
        return data
    except Exception as e:
        return {"error": str(e)}
