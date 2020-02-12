# walnut

CU Custom Pantheon Orchestration Tool

- [walnut](#walnut)
  - [Pre-requisites](#pre-requisites)
  - [Running Walnut](#running-walnut)
    - [Using Flask](#using-flask)
    - [Using uWSGI](#using-uwsgi)
  - [pipenv Common Commands](#pipenv-common-commands)

## Pre-requisites

* Install Python 3.7 [Homebrew](https://docs.python-guide.org/starting/install3/osx/)
* Install and start MongoDB 4.2 [Homebrew](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/)
* Install pipenv
  
    ```shell
    pip install pipenv
    ```

* Create a virtual environment inside at root of the project, this will also install the requirements in the `Pipfile`

  ```shell
  pipenv shell
  ```

## Running Walnut

### Using Flask

* Create a file in the root directory of this project named  `.env` with the following environmental variables:

  ```python
    FLASK_DEBUG = 1
    FLASK_APP = run.py
  ```

  The `.env` file is loaded after activating the virtual environment using `pipenv shell`

   Start a local development server:

   ```shell
   flask run
   ```

### Using uWSGI

  ```sh
  uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi
  ```

## pipenv Common Commands

Install a package

```shell
pipenv install flask
```

You can also specify a specific version

```shell
pipenv install flask==0.12.1
```

Install a package for development (not used in production)

```shell
pipenv install pytest --dev
```

Once everything is working and are ready to push to production lock the environment

```shell
pipenv lock
```

Uninstall a package, `Pipfile` is rebuilt automatically

```shell
pipenv uninstall numpy
```

Uninstall all packages, `Pipfile` is rebuilt automatically

```shell
pipenv uninstall --all
pipenv uninstall --all-dev
```

Location of a project's virtual environment

```shell
pipenv --venv
```
