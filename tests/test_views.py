
from rest_framework.test import APIClient


def test_get_data(client):
	c = APIClient()
	c.login("abd", "abc")
	result = c.get("data/")
	assert result

