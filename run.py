from eve import Eve
from auth import WalnutTokenAuth

app = Eve(auth=WalnutTokenAuth)

if __name__ == "__main__":
    app.run()
