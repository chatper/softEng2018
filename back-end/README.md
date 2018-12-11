# Solidity back-end

A python web application build on Flask

## Prerequisites
It is assumed that [python(v3.6+)](https://www.python.org/downloads/),  [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/) and [postgresql](https://www.postgresql.org/download/) are installed and running.
If there is not a database named `solidity` already created then go ahead and create it 
* Connect to local psql, for example for linux systems `sudo -u postgres -i` and then `psql`
* Create the database `create database solidity;`
* Exit the psql shell `\q`

If you used different credentials for the connection with the database, editi `.flaskenv` appropriately.

## Getting started
1. Navigate to the app's root directory `cd solidity/back-end`
2. Install, setup and activate [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
3. Install project dependencies `pip install -r requirements.txt`
4. Create and prepopulate the tables `flask init-db`
5. Run app `flask run`
