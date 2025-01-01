### `virtualenv venv`

Run the above command to create a Virtual Environment.

### `source venv/bin/activate`

Run the above command to activate the Virtual Environment.

### `pip install -r requirements`

Run the above command to install all the dependencies listed in the requirements.txt file.


# DATABASE SETUP
### `sudo -i -u postgres psql`

Use the above command to Login to PosgreSQL as Administrator. Make sure that you have PostgreSQL installed.

### `\password`

Use the above command to change the postgres User password to 'postgres'.

### `CREATE DATABASE vsms;`

Use the above command to create a new Database for the Project.


# PROJECT SETUP

### `python manage.py makemigrations`

Use the above command to create all Migrations Files.

### `python manage.py migrate`

Use the above command to Migrate the Database.

### `python manage.py createsuperuser`

Use the above command to create a Quick User for accessing the Application. Use the Super User username & password to Login to the Web Application.

### `python manage.py runserver 8000`

Use the above command to run the Development Server at PORT 8000.




