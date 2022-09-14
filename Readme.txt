Selenium_test

Parse
Site parsing takes place in the parse.py file in the 'parse_html()' function.

DataBase
In this project I used Postgresql.
To connect to database created engine. To do this I used path to Database:
'postgresql://postgres(It is username):1111(password)@localhost:5433/selenium_test'
Database functions:
create_db() - this function to create database
save_to_db() - this function to save data in database. Also I saved data to JSON file.
get_from_db() - this function to get data from db.

To check result of my parsing:
Run main file

To parse site with database:
1. Connect to Postgresql in file database.
2. Use function parse_html (this function returns data (list of dicts)).
3. Use functions to work with DB: create_db(), save_to_db(), get_from_db().


