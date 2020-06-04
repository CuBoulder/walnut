import json
import requests

def test_post_headers_body_json():
    url = "http://127.0.0.1:5000/instance"

    payload = 'sid=p1000000006&path=jesus-test-postman&instance_type=center&pantheon_site_id=1b0dc912-fd73-4ee3-b2e4-6718e0b3aebc&pantheon_size=xs&created_by=jeor0980'
    headers = {
        'Authorization': 'Bearer i51UOQB-d0rDd_O0qNFVUHaOgdbE2SV2z87fBNtsN9A',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # convert dict to json by json.dumps() for body data. 
    resp = requests.post(url, headers=headers, data=payload)
    print(resp.text)

    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 201
    # resp_body = resp.json()
    # assert resp_body['url'] == url

    # print response full body as text
    print(resp.text)
    print("taco")
