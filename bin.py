
# @app.route('/add_gateway', methods=['GET', 'POST'])
# def add_gateway():
#     if request.method == 'POST':
#         g_name = request.form.get('gateway_name')
#         g_id = request.form.get('gateway_id')
#         location = request.form.get('location')
#         gatewaydata(g_name, g_id, location)

#         # Send join request to LoRaWAN network server
#         join_data = {
#             "deveui": g_id,
#             "appeui": LORAWAN_APP_EUI,
#             "appkey": LORAWAN_APP_KEY
#         }
        
#         try:
#             response = requests.post(f"{LORAWAN_SERVER_URL}/join", json=join_data)
#             response.raise_for_status()

#             # Handle the response from the LoRaWAN server as needed
#             # For example, you might want to check if the join request was successful

#             return "Join request successful. Device joined the LoRaWAN network."

#         except requests.exceptions.RequestException as e:
#             return f"Error processing join request: {str(e)}"
        
 

#     return render_template('add_gateway.html', gateways=gateways)


  # # Example table creation query
    # table_name = "gateways"
    # create_table_query = """
    #     CREATE TABLE IF NOT EXISTS {} (
    #         name VARCHAR(255) NOT NULL,
    #         id VARCHAR(17) NOT NULL UNIQUE PRIMARY KEY,
    #         location VARCHAR(255) NOT NULL
    #     );
    # """.format(sql.Identifier(table_name))

    # Execute the query to create the table if it doesn't exist
    # cursor.execute(create_table_query)