"""Travis-CI Instance Enpoint Tests."""
import requests


class TestAccountsEndpoint:
    """Instance Endpoint test suite."""

    def test_get_accounts_endpoint(self):
        """Test that /accounts endpoint is returns 401 on unauthenticated GET request"""
        url = "http://127.0.0.1:5000/accounts"
        # convert dict to json by json.dumps() for body data.
        response = requests.get(url)

        # Validate response headers and body contents, e.g. status code.
        assert response.status_code == 401

        # print response full body as text
        print(response.text)
