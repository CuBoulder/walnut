import bcrypt
from eve.auth import BasicAuth, TokenAuth
from flask import current_app as app
import secrets


class BCryptAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        # use Eve's own db driver; no additional connections/resources are used
        accounts = app.data.driver.db['accounts']
        account = accounts.find_one({'username': username})
        return account and \
            bcrypt.hashpw(password, account['password']) == account['password']


class RolesAuth(TokenAuth):
    def check_auth(self, token,  allowed_roles, resource, method):
        # use Eve's own db driver; no additional connections/resources are used
        accounts = app.data.driver.db['accounts']
        lookup = {'token': token}
        if allowed_roles:
            # only retrieve a user if his roles match ``allowed_roles``
            lookup['roles'] = {'$in': allowed_roles}
        account = accounts.find_one(lookup)
        return account


def add_token(documents):
    """
    Appends a random string encoded in base64 format to a user document
    """
    # TODO: You should at least make sure that the token is unique.
    for document in documents:
        document["token"] = secrets.token_urlsafe()


def hash_password(documents):
    """
    Use bcrypt to hash user password before writing it to the database
    """
    for document in documents:
        salt = bcrypt.gensalt()
        document["password"] = bcrypt.hashpw(document["password"], salt)