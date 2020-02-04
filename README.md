# walnut

CU Custom Pantheon Orchestration Tool 

## Quickstart

* Install Python 3.7 [Homebrew](https://docs.python-guide.org/starting/install3/osx/)
* Install and start MongoDB 4.2 [Homebrew](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/)
* Create and activate a venv [Python Guide](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

  ```sh
  python3 -m venv env
  source env/bin/activate
  ```  

* Install requirements

  ```sh
  pip install -r requirements.txt
  ```

* Running the application locally via Flask

  ```sh
  # Debug mode allows live-reload to work
  FLASK_DEBUG=1 FLASK_APP=run.py flask run
  ```

* Running the application locally via uWSGI

  ```sh
  uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi
  ```

* Alternate Fish shell Quickstart

  ```sh
  python3 -m venv env
  source env/bin/activate.fish
  pip install -r requirements.txt
  env FLASK_DEBUG=1 FLASK_APP=run.py flask run
  ```

## Authentication

This application assumes there is a mongoDB database named `walnut` with a collection named `accounts`.

The initial user is created manually by inserting a document into `accounts`.

* Password must be stored as a bcrpyt hash

* Token should be generated using the Python 3.6+ secrets library.

* Initial user role should be set to `superuser`


## Endpoints

`instance`

`accounts`
