
from pymongo import MongoClient


client = MongoClient('mongodb://mongo')
db = client['Movies']
collection = db['Movie']


def db_add_movie(instance):
    movie_data = {
        '_id': instance.id,
        'name': instance.name,
        'protagonists': instance.protagonists,
        'poster': instance.poster.url,
        'start_date': instance.start_date,
        'status': instance.status,
        'ranking': instance.ranking
    }
    collection.insert_one(movie_data)


def db_edit_movie(instance):
    movie_data = {
        'name': instance.name,
        'protagonists': instance.protagonists,
        'poster': instance.poster.url,
        'start_date': instance.start_date,
        'status': instance.status,
        'ranking': instance.ranking
    }
    collection.update_one({'_id': instance.id}, {"$set": movie_data})


def db_retrieve_all_movie():
    return [each for each in collection.find()]
