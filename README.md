# grocery_store_with_flask
This site is simple online store with the functionality of registration, authorization, creating and deleting an order
## Stack
- Flask
- Jinja
- PostgreSQL
## Represitory overview
- config/ - 
  - .env.dist - file with environment variables for distribution 
  - config.py - py file for environment variables
- template/ - folder for HTML template
- app.py - main py file with routs and app
- model.py - py file with models for db
- schema.sql - file with database queries
- README.md - file with describe project
- test_unittest.py - py file with script for testing the function login()
## To start a project (for Windows10)
1. install git
2. take git repository
  - `$ git clone https://github.com/gygever/grocery_store_with_flask.git`
3. go to project folder
4. install dependencies from requirements.txt
  - `$ py -m pip install -r requirements.txt`
5. run app
  - `$ flask --app app run`
## To start a project (Ubuntu Mate 22.04.3)
1. install git
2. take git repository
  - `$ git clone https://github.com/gygever/grocery_store_with_flask.git`
3. go to project folder
4. install dependencies from requirements.txt
  - `$ python3 -m pip install -r requirements.txt`
  - if you get `Error: pg_config executable not found`, write `$ sudo apt-get install libpq_dev` and try to install requirements again 
5. run app
  - `$ python3 -m flask --app app run`
## Webapp design
<img src='https://sun9-61.userapi.com/impg/gJFNmz72pwNf7qGya21-JHvpJyWOETclsVBocg/cWbfNg53PUs.jpg?size=1405x907&quality=96&sign=b34ebeac366d0b341d1af1274f62c245&type=album'>