from eve import Eve
from eve.auth import BasicAuth
from flask import g
import os

class MyBasicAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource,
                   method):
        return username == os.environ['mu'] and password == os.environ['mp']

app = Eve(auth=MyBasicAuth)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
