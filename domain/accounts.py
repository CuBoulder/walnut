from auth import RolesAuth


accounts = {
    'authentication': RolesAuth,
    'public_methods': [],
    'resource_methods': ['GET', 'POST'],
    'hateoas': False,
    # the standard account entry point is defined as
    # '/accounts/<ObjectId>'. We define  an additional read-only entry
    # point accessible at '/accounts/<username>'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'username',
    },

    # We also disable endpoint caching as we don't want client apps to
    # cache account data.
    "cache_control": "",
    "cache_expires": 0,

    # Allow 'token' to be returned with POST responses
    'extra_response_fields': ['token'],

    # Only allow superusers and admins.
    'allowed_roles': ['superuser', 'admin'],

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
        'roles': {
            'type': 'string',
            'allowed': ['user', 'superuser', 'admin'],
            'required': True,
        },
        'token': {
            'type': 'string'
        }
    }
}
