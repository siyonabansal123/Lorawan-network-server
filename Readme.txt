Steps to use this flask application locally on your device:



Create a virtual Environment : 

1. pip install virtualenv
2. virtualenv venv
3. To Activate the venv : On Windows: .\venv\Scripts\activate, On Unix or MacOS: source venv/bin/activate
4. Deactivate the virtual environment: deactivate
5. install flask
6. install pandas


PostgreSQL set-up : (Chirpstack uses PostgreSQL type database)

Windows:
Visit the official PostgreSQL download page: https://www.postgresql.org/download/
Choose the version suitable for your Windows system and download the installer.
Run the installer and follow the on-screen instructions.
Configure PostgreSQL: During the installation, you will be prompted to set a password for the default PostgreSQL user (postgres). Remember this password, as you will need it later.
Start PostgreSQL Service: PostgreSQL service should start automatically after installation. If not, you can start it manually from the Services application.
Verify Installation: Open a command prompt or PowerShell and run psql. If successful, you'll be connected to the PostgreSQL command-line interface.

Linux:
Open a terminal and update the package lists: sudo apt update
Install PostgreSQL using the package manager for your distribution. For example, on Ubuntu: sudo apt install postgresql postgresql-contrib
PostgreSQL creates a default user called "postgres." Set a password for this user: sudo -u postgres psql
\password postgres
Start the PostgreSQL service and enable it to start on boot: sudo service postgresql start
sudo systemctl enable postgresql
Access the PostgreSQL command-line interface to verify the installation:  sudo -u postgres psql

****
Post-installation steps (for all operating systems):
1. Access the PostgreSQL command line by running: psql -U postgres
2. You can create a new user and a new database using SQL commands. : CREATE USER nanosniff WITH PASSWORD 'password';
CREATE DATABASE sensor_data;
CREATE DATABASE all_data;
ALTER DATABASE sensor_data OWNER TO nanosniff;
ALTER DATABASE all_data OWNER TO nanosniff;
3. Then create tables using the first function in the function.py file

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nanosniff:password@localhost/sensor_data'
****



Chirpsatck set-up :

1. Install Docker : https://www.chirpstack.io/docs/getting-started/docker.html
2. In the terminal, run the following command to start ChirpStack Network Server: docker-compose up -d
3. You can access the ChirpStack Network Server web interface at http://localhost:8080 in your web browser.
4. Create API key and replace it in the function.py file in create_chirpstack_gateway() function
