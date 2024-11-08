# backend/app/config.py
class Config:
    MYSQL_HOST = 'localhost'  # MySQL host (usually 'localhost')
    MYSQL_USER = 'root'  # MySQL username (default is 'root')
    MYSQL_PASSWORD = ''  # MySQL password (replace with your actual MySQL password)
    MYSQL_DB = 'food_waste_db'  # Database name
    MYSQL_CURSORCLASS = 'DictCursor'  # To get results in dictionary format

