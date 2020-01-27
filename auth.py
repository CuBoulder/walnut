from eve import Eve
from eve.auth import BasicAuth, TokenAuth
from werkzeug.security import check_password_hash
from flask import current_app as app


class WalnutTokenAuth(TokenAuth):
    def check_auth(self, token, allowed_roles, resource, method):
        """
        :param token: decoded user name.
        :param allowed_roles: allowed user roles
        :param resource: resource being requested.
        :param method: HTTP method being executed(POST, GET, etc.)
        """

        # use Eve's own db driver; no additional connections/resources are used
        accounts = app.data.driver.db['accounts']
        return accounts.find_one({'token': token})


class Sha1Auth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        # use Eve's own db driver; no additional connections/resources are used
        accounts = app.data.driver.db['accounts']
        account = accounts.find_one({'username': username})
        return account and \
            check_password_hash(account['password'], password)
