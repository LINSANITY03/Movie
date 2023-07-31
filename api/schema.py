from ninja import ModelSchema, File, Schema
from ninja.files import UploadedFile
from .models import *


class MovieSchema(ModelSchema):

    class Config:
        model = Movie
        model_fields = ['name', 'protagonists',
                        'start_date', 'status', 'ranking']


class RetrieveMovieSchema(ModelSchema):

    class Config:
        model = Movie
        model_fields = ['id', 'name', 'protagonists',
                        'start_date', 'status', 'ranking']
