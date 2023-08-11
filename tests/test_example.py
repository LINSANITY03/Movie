from api.models import Movie

from django.core.files import File
from unittest import mock
import pytest

pytestmark = pytest.mark.django_db

image_mock = mock.MagicMock(spec=File)
image_mock.name = "movie_poster.png"


@pytest.fixture()
def movie(db) -> Movie:
    return Movie.objects.create(name="Oppenheimer", protagonists=["cillian", "jean"], poster=image_mock)


@pytestmark
def test_create_movie(movie):
    assert Movie.objects.exists() == True
