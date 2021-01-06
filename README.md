# Steps to run locally
1. `cd backend` to go in the direcotry.
2. `python3 -m venv env` to create the virtual env.
3. `source env/bin/activate` to activate the environment.
4. `pip install -r requirements.text` to install the requirements.

## Improvements
1. Use `environment variable` to load the google client id, very bad to hardcode.
2. User `Provider Type` as a different table and make a one to many relatiosnhip with NetworkProviders.
3. Use PostgreSQL instead of SQLite in production.
