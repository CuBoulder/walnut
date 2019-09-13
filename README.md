# walnut

CU Custom Pantheon Orchestration Tool 

## Quickstart

* Install Python 3.7 [Homebrew](https://docs.python-guide.org/starting/install3/osx/)
* Install and start MongoDB 4.2 [Homebrew](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/)
* Create and activate a virtualenv [Python Guide](https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv)
* Install requirements
  ```sh
  pip install -r requirements.txt
  ```
* Start Flask
  ```sh
  # Debug mode allows live-reload to work
  FLASK_DEBUG=1 FLASK_APP=run.py flask run
  ```
