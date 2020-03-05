"""Walnut Authentication Methods."""

import secrets
import bcrypt
from eve.auth import BasicAuth, TokenAuth
from flask import current_app as app


class BCryptAuth(BasicAuth):
    """Custom authentication logic is provided by a subclass of eve.auth.BasicAuth."""

    def check_auth(self, username, password, allowed_roles, resource, method):
        """Check if a username and password combination is valid."""
        # Use Eve's own db driver; no additional connections/resources are used
        accounts = app.data.driver.db['accounts']
        account = accounts.find_one({'username': username})
        return account and \
            bcrypt.hashpw(password, account['password']) == account['password']


class RolesAuth(TokenAuth):
    """Custom authentication logic is provided by a subclass of eve.auth.BasicAuth."""

    def check_auth(self, token, allowed_roles, resource, method):
        """Check if a token and role combination is valid."""
        # use Eve's own db driver; no additional connections/resources are used
        accounts = app.data.driver.db['accounts']
        lookup = {'token': token}
        if allowed_roles:
            # only retrieve a user if his roles match ``allowed_roles``
            lookup['roles'] = {'$in': allowed_roles}
        account = accounts.find_one(lookup)
        return account


def add_token(documents):
    """Generate and insert authentication token to a document.

    Generates and inserts a random string encoded in base64 format to passed in document(s)
    """
    # TODO: You should at least make sure that the token is unique.
    for document in documents:
        document["token"] = secrets.token_urlsafe()


def hash_password(documents):
    """Use bcrypt to hash user password before writing it to the database."""
    for document in documents:
        salt = bcrypt.gensalt()
        document["password"] = bcrypt.hashpw(document["password"], salt)


def look_up_user_by_token(token):
    """Return username tied to an auth token."""
    accounts = app.data.driver.db['accounts']
    account = accounts.find_one({'token': token})
    return account["username"]
