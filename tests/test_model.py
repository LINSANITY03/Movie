from api.models import Movie

from django.contrib.auth.models import User
from django.core.files import File
from django.conf import settings
from unittest import mock
import pytest
import psycopg2


image_mock = mock.MagicMock(spec=File)
image_mock.name = "movie_poster.png"


@pytest.fixture()
def django_db_setup():
    connection = psycopg2.connect(
        database="Movies",
        user="postgres", password="postgresql1234",
        host="127.0.0.1", port=5432)
    return connection.cursor()


def test_user(django_db_setup):
    django_db_setup.execute(
        User.objects.create(
            username="pujan", email="pujan@gmail.com", password="pujanpujan"))
    assert Movie.objects.exists() == True
