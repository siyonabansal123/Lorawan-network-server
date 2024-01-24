from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def display_table_names():
    conn = sqlite3.connect('./mydatabase.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    conn.close()
    
    return [table[0] for table in tables] if tables else []

@app.route('/')
def index():
    return render_template('home.html', tables=display_table_names())

@app.route('/data', methods=['POST'])
def display_data():
    selected_table = request.form.get('table_name')
    num_rows = int(request.form.get('num_rows', 10))
    conn = sqlite3.connect('./mydatabase.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {selected_table} LIMIT {num_rows};")
    table_data = cursor.fetchall()
    conn.close()
    return render_template('data.html', selected_table=selected_table, table_data=table_data, num_rows=num_rows, tables=display_table_names())

import requests


# Replace these values with your LoRaWAN network server details
LORAWAN_SERVER_URL = 'https://your-lorawan-server/api'
LORAWAN_APP_EUI = 'your-application-eui'
LORAWAN_APP_KEY = 'your-application-key'

def insert_gateway_into_db(name, mac_address, location):
    conn = sqlite3.connect('all_data.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO gateways (name, mac_address, location) VALUES (?, ?, ?)', (name, mac_address, location))
    conn.commit()
    conn.close()

@app.route('/add_gateway', methods=['GET', 'POST'])
def add_gateway():
    if request.method == 'POST':
        g_name = request.form.get('gateway_name')
        mac_address = request.form.get('gateway_mac')
        location = request.form.get('location')
        insert_gateway_into_db(g_name, mac_address, location)

        # Send join request to LoRaWAN network server
        join_data = {
            "deveui": mac_address,
            "appeui": LORAWAN_APP_EUI,
            "appkey": LORAWAN_APP_KEY
        }
        
        try:
            response = requests.post(f"{LORAWAN_SERVER_URL}/join", json=join_data)
            response.raise_for_status()

            # Handle the response from the LoRaWAN server as needed
            # For example, you might want to check if the join request was successful

            return "Join request successful. Device joined the LoRaWAN network."

        except requests.exceptions.RequestException as e:
            return f"Error processing join request: {str(e)}"
        
    conn = sqlite3.connect('all_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM gateways')
    gateways = cursor.fetchall()
    conn.close()

    return render_template('add_gateway.html', gateways=gateways)



@app.route('/add_sensors')
def add_sensors():
    return render_template('add_sensors.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)

