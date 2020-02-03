from eve import Eve
from auth import BCryptAuth, RolesAuth, add_token

app = Eve()
app.on_insert_accounts += add_token

if __name__ == "__main__":
    app.run()
