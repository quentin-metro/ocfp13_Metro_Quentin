from django.urls import reverse
from django.test import Client
import pytest
from .models import Profile


@pytest.mark.django_db
def test_index_profiles(client):
    client = Client()
    path = reverse('profiles_index')
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<title>Profiles</title>"
    assert response.status_code == 200
    assert expected_content in content


@pytest.mark.django_db
def test_profile(client):
    client = Client()
    profile_list = Profile.objects.all()
    if profile_list:
        profile = profile_list[0]
        path = reverse('letting', args=[profile.pk])
        response = client.get(path)
        content = response.content.decode()
        expected_content = f"<title>{profile.user.username}</title>"
        assert response.status_code == 200
        assert expected_content in content
