from django.urls import reverse
from django.test import Client
import pytest

from .models import Letting


@pytest.mark.django_db
def test_index_lettings(client):
    client = Client()
    path = reverse('lettings_index')
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<title>Lettings</title>"
    assert response.status_code == 200
    assert expected_content in content


@pytest.mark.django_db
def test_letting(client):
    client = Client()
    letting_list = Letting.objects.all()
    if letting_list:
        letting = letting_list[0]
        path = reverse('letting', args=[letting.pk])
        response = client.get(path)
        content = response.content.decode()
        expected_content = f"<title>{Letting.title}</title>"
        assert response.status_code == 200
        assert expected_content in content
