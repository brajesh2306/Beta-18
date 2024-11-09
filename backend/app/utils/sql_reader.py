def fetch_sql_data(mysql):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM food_consumption")
    food_data = cursor.fetchall()

    cursor.execute("SELECT * FROM inventory")
    inventory_data = cursor.fetchall()

    cursor.close()

    return {"food_consumption": food_data, "inventory": inventory_data}