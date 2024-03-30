import mysql.connector
import json

# Load MySQL connection parameters from a separate configuration file
from config import mysql_config

# Function to read data from JSON file
def read_json_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

# Function to insert data into the petlebi table
def insert_data_into_mysql(data):
    try:
        connection = mysql.connector.connect(**mysql_config)
        cursor = connection.cursor()

        # Example SQL query to insert data into the petlebi table
        sql_query = "INSERT INTO petlebi (url, name, barcode, price, stock, images, description, category, brand) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

        for item in data:
            # Execute the SQL query
            cursor.execute(sql_query, (
                item['url'],
                item['name'],
                item['barcode'],
                item['price'],
                item['stock'],
                json.dumps(item['images']),
                item['description'],
                item['category'],
                item['brand']
            ))

        # Commit changes to the database
        connection.commit()
        print("Data inserted successfully")

    except mysql.connector.Error as error:
        print("Failed to insert data into MySQL table:", error)

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()

def main():
    json_filename = 'petlebi_products.json'
    data = read_json_file(json_filename)
    insert_data_into_mysql(data)

if __name__ == "__main__":
    main()
