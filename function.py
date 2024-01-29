import psycopg2
from psycopg2 import sql
import requests
import pandas as pd


def create_table(table_name):
    # Replace these with your own database connection details
    dbname = "all_data"
    user = "nanosniff"
    password = "password"
    host = "localhost"
    port = "5432"

    # Connect to the PostgreSQL database
    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Define the SQL query to create a table
    create_table_query = sql.SQL("""
        CREATE TABLE IF NOT EXISTS {} (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            location VARCHAR(255)
        )
    """).format(sql.Identifier(table_name))

    try:
        # Execute the SQL query
        cursor.execute(create_table_query)
        # Commit the changes
        connection.commit()
        print(f"Table '{table_name}' created successfully.")
    except Exception as e:
        # Rollback the transaction in case of an error
        connection.rollback()
        print(f"Error: {e}")
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()

def get_table_names():
    # Replace these values with your PostgreSQL connection details
    dbname = "sensor_data"
    user = "nanosniff"
    password = "password"
    host = "localhost"
    
     # Connect to the PostgreSQL database
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    cursor = conn.cursor()

    # Get all table names in the public schema
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
    table_names = [row[0] for row in cursor.fetchall()]

    # Close the cursor and connection
    cursor.close()
    conn.close()
    return table_names

def get_table_data(table_name, num_rows):
    dbname = "sensor_data"
    user = "nanosniff"
    password = "password"
    host = "localhost"
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    cursor = conn.cursor()

    # Query to get the specified number of rows from the selected table
    query = f"SELECT * FROM {table_name} LIMIT {num_rows};"

    cursor.execute(query)
    table_data = cursor.fetchall()

    cursor.close()
    conn.close()

    return table_data

def gatewaydata(g_name, g_id, location):
    # Replace these values with your PostgreSQL connection details
    dbname = "all_data"
    user = "nanosniff"
    password = "password"
    host = "localhost"

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    cursor = conn.cursor()
    
    # SQL query to insert data into the "gateways" table (replace with your actual table name)
    insert_query = "INSERT INTO gateways (name, id, location) VALUES (%s, %s, %s);"

    # Execute the query with the data
    cursor.execute(insert_query, (g_name, g_id, location))
    # Commit the changes
    conn.commit()
    # Close the cursor and connection
    cursor.close()
    conn.close()
    
def gatewaylist():
    db_connection = psycopg2.connect(
    dbname="all_data",
    user="nanosniff",
    password="password",
    host="localhost",
    port="5432"
    )
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM gateways;")
    data = cursor.fetchall()
    cursor.close()
    return data
    
# def add_gateway_to_chirpstack(name, mac_address, location):
#     chirpstack_api_url = 'http://chirpstack-api-url'
#     payload = {
#         'name': name,
#         'mac': mac_address,
#         'location': location,
#         # Add other required parameters
#     }
    

#     response = requests.post(f'{chirpstack_api_url}/api/gateways', json=payload)

#     if response.status_code == 200:
#         print('Gateway added to ChirpStack successfully')
#     else:
#         print(f'Failed to add gateway to ChirpStack. Status Code: {response.status_code}')

import requests

def create_chirpstack_gateway(g_name, g_id, location):
    CHIRPSTACK_API_URL = "http://your-chirpstack-server:8080/api"
    url = f"{CHIRPSTACK_API_URL}/gateways"
    headers = {
        # add your API Key here!
        "Grpc-Metadata-Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjaGlycHN0YWNrIiwiaXNzIjoiY2hpcnBzdGFjayIsInN1YiI6IjY1NjM1NTU4LWZiMmMtNDgwMC04NGI1LTczMmU1NzJjZDBlMiIsInR5cCI6ImtleSJ9.ZPLBLpvNDxBj-6BaglIO2Mk4GImgDEYOEbyj_8B-njM"
    }

    data = {
        "name": g_name,
        "id": g_id,
        "location": location,
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        print(f"Gateway '{g_name}' added successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")