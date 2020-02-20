"""Walnut API Domain Definition, stored as a dictionary."""

from .instance import instance
from .accounts import accounts

DOMAIN = {
    "instance": instance,
    "accounts": accounts
}
