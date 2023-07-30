from ninja import ModelSchema
from .models import *


class MovieSchema(ModelSchema):

    class Config:
        model = Movie
        model_fields = ['name', 'protagonists', 'start_date', 'status', 'ranking']