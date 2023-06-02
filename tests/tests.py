from django.urls import reverse
from django.test import Client


def test_index(client):
    client = Client()
    path = reverse('index')
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<title>Holiday Homes</title>"
    assert response.status_code == 200
    assert expected_content in content
