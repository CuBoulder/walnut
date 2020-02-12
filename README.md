# walnut

CU Custom Pantheon Orchestration Tool

## Quickstart

* Install Python 3.7+ [Homebrew](https://docs.python-guide.org/starting/install3/osx/)
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

This application requires a MongoDB database named `walnut` with a collection named `accounts` for user management.

Available user roles are `user`, `developer`, `admin`.

The initial user is created manually by inserting a document into `accounts`.

### Creating the admin user

1. Generate a hashed password using the Python3 library `bcrypt`

    * Start the Python shell

      ```shell
      python
      ```

    * Run the following commands:

      ```python
      import bcrypt

      print(bcrypt.hashpw("password_to_be_hashed", bcrypt.gensalt()))
      ```

      Save the hashed value that is printed for the next step.

2. Use the following Mongo CLI Commands to create the `admin` user:

    * Start the mongo shell

      ```shell
      mongo
      ```

    * Run the following commands:

      ```mongodb
      use walnut

      db.createCollection(accounts)

      db.accounts.insert({
        username: 'admin',
        password: 'hashed_password_from_step_1',
        role: 'admin'
      })
      ```

3. Create separate developer user

Send a POST request to create your own account using `curl`

  ```shell
  curl -u admin -d '{"username":"identikey", "password":"your_password", "role":"developer"}' -H "Content-Type: application/json" -X POST http://localhost:5000/accounts
  ```



## Endpoints

### instance

Description: The collection of Express instances hosted on Pantheon

Public Methods: `GET`

Authentication: `Token Auth`

Authenticated Methods: `POST, DELETE`

### accounts

Authentication: `Basic Auth (Username, Password)`

Authenticated Methods: `POST, DELETE`
