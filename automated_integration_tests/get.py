import requests
import pytest

def test_get_locations_for_us_90210_check_status_code_equals_200():
    response = requests.post("http://localhost:8888/api/blog/categories/")
    response_body = response.json()
    pytest.set_trace()
    assert response.status_code == 200