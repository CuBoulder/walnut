import os

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

DOMAIN = {
    "instance": {
        "public_methods": ["GET"],
        "public_item_methods": ["GET"],
        "versioning": True,
        "soft_delete": True,
        # Allow lookup by 'sid' in addition to '_id'.
        "additional_lookup": {"url": 'regex("[\w]+")', "field": "sid"},
        "schema": {
            # TODO: Should we use this in the unique names for Pantheon and subdomains that we need for the Advanced CDN? Maybe something like: ucb-[sid].colorado.edu
            # TODO: Talk with NEO about the best way to handle requests for a thousand subdomains.
            "sid": {"type": "string", "minlength": 9, "maxlength": 14, "unique": True},
            "tag": {"type": "list"},
            # TODO: Path + instance type needs to be unique
            "path": {"type": "string"},
            # TODO: Verify that there is a 1 to 1 (or many to 1) correlation between 'instance_type' and public subdomain
            # IE 'labs' => 'labs.colorado.edu'; 'college', 'school', and 'academic_program' all running under 'www.colorado.edu' should also be straight forward
            # If a single 'instance_type' should be run under multiple different subdomains, we will probably need another field.
            "instance_type": {
                "type": "string",
                "allowed": [
                    "college",
                    "school",
                    "academic_department",
                    "academic_program",
                    "academic_support",
                    "certificate_program",
                    "outreach_program",
                    "residential_academic_program",
                    "center",
                    "institute",
                    "service_department",
                    "resource_department",
                    "support_department",
                    "performance",
                    "events",
                    "museum",
                    "research_program",
                    "lab",
                    "faculty",
                    "student_group",
                    "student_government",
                    "sport_club",
                    "publication",
                    "initiative",
                    "marketing",
                    "committee",
                    "course",
                    "project",
                    "adminstration",
                    "facility",
                ],
            },
            "pantheon_size": {
                "type": "string",
                "allowed": ["xs", "s", "m", "l", "xl", "e"],
            },
            "cse_creator": {"type": "string"},
            "cse_id": {"type": "string"},
            "google_tag_client_container_id": {"type": "string"},
        },
    }
}

