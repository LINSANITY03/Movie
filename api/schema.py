from ninja import ModelSchema
from .models import *


class MovieSchema(ModelSchema):
    _id: int

    class Config:
        model = Movie
        model_fields = ['name', 'protagonists', 'poster', 'start_date', 'status', 'ranking']