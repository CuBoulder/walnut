import os
from domain import DOMAIN
from auth import Sha1Auth


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
