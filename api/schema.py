from ninja import ModelSchema, File
from ninja.files import UploadedFile
from .models import *


class MovieSchema(ModelSchema):

    class Config:
        model = Movie
        model_fields = ['name', 'protagonists',
                        'start_date', 'status', 'ranking']


class MovieEditSchema(ModelSchema):

    class Config:
        model = Movie
        model_fields = ['name', 'protagonists',
                        'start_date', 'status', 'ranking']
