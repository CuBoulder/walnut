"""Travis-CI Instance Enpoint Tests."""
import requests


class TestInstanceEndpoint:
    """Instance Endpoint test suite."""

    def test_get_instance_endpoint(self):
        """Test that /instance endpoint is working and returns a 200 response."""
        url = "http://127.0.0.1:5000/instance"
        # convert dict to json by json.dumps() for body data.
        response = requests.get(url)

        # Validate response headers and body contents, e.g. status code.
        assert response.status_code == 200

        # print response full body as text
        print(response.text)
