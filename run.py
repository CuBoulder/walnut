"""Walnut Launch Script."""

from eve import Eve
from auth import add_token, hash_password

app = Eve()
app.on_insert_accounts += add_token
app.on_insert_accounts += hash_password

if __name__ == "__main__":
    app.run()
