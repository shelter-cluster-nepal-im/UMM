import os

DOMAIN = {'people': {}}
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USERNAME = os.environ['mu'] 
MONGO_PASSWORD = os.environ['mp']
MONGO_DBNAME = 'umm_api'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
