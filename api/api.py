from ninja import Router, UploadedFile, File, Form

from django.shortcuts import get_object_or_404
from django.db import transaction

from .schema import MovieSchema
from .models import Movie
from .mongo_db import db_add_movie, db_edit_movie


router = Router()


@router.post('/add_movie')
def add_movie(request, payload: MovieSchema = Form(...), poster: UploadedFile = File(...)):

    try:
        new_record = Movie.objects.create(**payload.dict(), poster=poster)
        db_add_movie(new_record)
        return 200, {"message": "Data has successfully been added"}
    except:
        return 400, {"message": "Data entry failed"}


@router.post('/edit_movie/{movie_id}')
def edit_movie(request, movie_id, payload: MovieSchema = Form(...), poster: UploadedFile = File(...)):

    with transaction.atomic():
        new_record = get_object_or_404(Movie, pk=movie_id)
        new_record.name = payload.name
        new_record.protagonists = payload.protagonists
        new_record.start_date = payload.start_date
        new_record.status = payload.status
        new_record.ranking = payload.ranking
        new_record.poster = poster
        new_record.save()

        db_edit_movie(new_record)

        return 200, {"message": "Data has successfully been Updated"}
