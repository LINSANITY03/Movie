from ninja import Router, UploadedFile, File, Form
from .schema import MovieSchema
from .models import Movie
from pymongo import MongoClient

router = Router()


@router.post('/add_movie')
def add_movie(request, payload: MovieSchema = Form(...), poster: UploadedFile = File(...)):
    new_record = Movie.objects.create(**payload.dict(), poster=poster)
    client = MongoClient('localhost', 27017)
    db = client['Movies']
    collection = db['Movie']
    movie_data = {
        '_id': new_record.id,
        'name': new_record.name,
        'protagonists': new_record.protagonists,
        'poster': new_record.poster.url,
        'start_date': new_record.start_date,
        'status': new_record.status,
        'ranking': new_record.ranking
    }
    collection.insert_one(movie_data)
    client.close()
