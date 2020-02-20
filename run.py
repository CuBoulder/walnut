"""Walnut Launch Script."""

from eve import Eve
from auth import add_token, hash_password

APP = Eve()
APP.on_insert_accounts += add_token
APP.on_insert_accounts += hash_password

if __name__ == "__main__":
    APP.run()
