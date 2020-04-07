"""Walnut Eve API Settings."""

import os
from domain import WALNUT_DOMAINS

DOMAIN = WALNUT_DOMAINS
# GCP Hosting mongodb settings
if os.environ.get('GCP_WALNUT_PROD'):
    MONGO_HOST = os.environ.get("MONGO_HOST", "example_mongo_server_ip")
    MONGO_PORT = os.environ.get("MONGO_PORT", "example_mongo_port")
    MONGO_DBNAME = os.environ.get("MONGO_DBNAME", "walnut")
    MONGO_USERNAME = "example_user"
    MONGO_PASSWORD = "exmaple_mongo_password"
    MONGO_AUTH_SOURCE = "example_mongo_auth_source"
    MONGO_OPTIONS = {"connect": True, "tz_aware": True, "tls": True,
                     "tlsAllowInvalidCertificates": True}
else:
    # Local development mongodb settings
    MONGO_HOST = os.environ.get("MONGO_HOST", "localhost")
    MONGO_PORT = os.environ.get("MONGO_PORT", 27017)
    MONGO_DBNAME = os.environ.get("MONGO_DBNAME", "walnut")
# Allow $regex filtering. Default config blocks where and regex.
MONGO_QUERY_BLACKLIST = ["$where"]

DATE_FORMAT = "%Y-%m-%d %H:%M:%S GMT"

# Read-only, unless authenticated
PUBLIC_METHODS = ["GET"]
# See a list of all items in a resource, allow new items to be created.
RESOURCE_METHODS = ["GET", "POST"]
# See an item, update field, replace the record, delete the record.
ITEM_METHODS = ["GET", "PATCH", "PUT", "DELETE"]
# Require etags in update and delete requests, serves as concurency control.
ENFORCE_IF_MATCH = True
