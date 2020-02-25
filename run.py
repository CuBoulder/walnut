"""Walnut Launch Script."""
# pylint: disable=no-member

from eve import Eve
from auth import add_token, hash_password

WALNUT = Eve()
WALNUT.on_insert_accounts += add_token
WALNUT.on_insert_accounts += hash_password

if __name__ == "__main__":
    WALNUT.run()
