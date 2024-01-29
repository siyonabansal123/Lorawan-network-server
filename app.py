from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from function import get_table_names, get_table_data, gatewaydata, gatewaylist, create_chirpstack_gateway
import pandas as pd


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html', tables=get_table_names())


@app.route('/data', methods=['POST'])
def display_data():
    selected_table = request.form.get('table_name')
    num_rows = int(request.form.get('num_rows', 10))
    table_data = get_table_data(selected_table, num_rows)
    return render_template('data.html', selected_table=selected_table, table_data=table_data, num_rows=num_rows, tables=get_table_names())


@app.route('/add_gateway', methods=['GET', 'POST'])
def add_gateway():
    if request.method == 'POST':
        g_name = request.form.get('gateway_name')
        g_id = request.form.get('gateway_id')
        location = request.form.get('location')
        gatewaydata(g_name, g_id, location)
        create_chirpstack_gateway(g_name, g_id, location)
    gateways = (gatewaylist())
    
    return render_template('add_gateway.html', gateways = gateways)


@app.route('/add_sensors')
def add_sensors():
    return render_template('add_sensors.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)

