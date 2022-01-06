from chalice.test import Client
from app import app


def test_get_produce():
    with Client(app) as client:
        response = client.http.get('/produce')
        assert response.json_body == {'produce': 'produce'}
