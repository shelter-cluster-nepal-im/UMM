import os

MONGO_HOST = 'localhost'
MONGO_PORT = 27017 
MONGO_USERNAME = os.environ['mu'] 
MONGO_PASSWORD = os.environ['mp']
MONGO_DBNAME = 'ummapi'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

ag_request = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'additional_lookup': { 'url': 'regex("[\w]+")', 'field': 'name' },
    'schema': {
       'name': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 100,
            'required': True,
            'unique': True,
        },
        'email': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 100,
            'required': True,
            'unique': True,
        },
        'agency_name': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 100,
            'required': True,
            'unique': True,
        },
        'designation': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 100,
            'required': True,
            'unique': True,
        },
        'deployment': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 100,
            'required': True,
            'unique': True,
        },
    }   
}

DOMAIN = {'ag_request' : ag_request,}
