from ninja import ModelSchema
from .models import *


class MovieSchema(ModelSchema):

    class Config:
        model = Movie
        model_fields = ['id', 'name', 'protagonists', 'poster', 'start_date', 'status', 'ranking']