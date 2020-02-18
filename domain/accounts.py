from auth import BCryptAuth


accounts = {
    'authentication': BCryptAuth,
    'public_methods': [],
    'resource_methods': ['GET', 'POST'],
    'hateoas': False,
    # the standard account entry point is defined as
    # '/accounts/<ObjectId>'. We define  an additional read-only entry
    # point accessible at '/accounts/<username>'.
    'additional_lookup': {
        'url': r'regex("[\w]+")',
        'field': 'username',
    },

    # We also disable endpoint caching as we don't want client apps to
    # cache account data.
    "cache_control": "",
    "cache_expires": 0,

    # Allow 'token' to be returned with POST responses
    'extra_response_fields': ['token'],

    # Only allow developers and admins.
    'allowed_roles': ['developer', 'admin'],

    # Finally, let's add the schema definition for this endpoint.
    'schema': {
        'username': {
            'type': 'string',
            'required': True,
            'unique': True,
        },
        'password': {
            'type': 'string',
            'required': True,
        },
        'role': {
            'type': 'string',
            'allowed': ['user', 'developer', 'admin'],
            'required': True,
        },
        'token': {
            'type': 'string'
        }
    }
}
