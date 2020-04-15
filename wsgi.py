"""Launch Script for WSGI Server."""

from run import WALNUT as application

if __name__ == "__main__":
    application.run(host="0.0.0.0")
