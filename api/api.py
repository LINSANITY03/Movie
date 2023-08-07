from ninja import Router, UploadedFile, File, Form

from django.shortcuts import get_object_or_404
from django.db import transaction
from typing import List
from .schema import MovieSchema, RetrieveMovieSchema
from .models import Movie
from .mongo_db import db_add_movie, db_edit_movie, db_retrieve_all_movie
from .tasks import increment_ranks


router = Router()


@router.post('/add_movie')
def add_movie(request, payload: MovieSchema = Form(...), poster: UploadedFile = File(...)):

    try:
        # create record on postgresql
        new_record = Movie.objects.create(**payload.dict(), poster=poster)

        # create record on mongodb
        db_add_movie(new_record)

        return 200, {"message": "Data has successfully been added"}
    except:
        return 400, {"message": "Data entry failed"}


@router.post('/edit_movie/{movie_id}')
def edit_movie(request, movie_id, payload: MovieSchema = Form(...), poster: UploadedFile = File(...)):

    try:
        with transaction.atomic():

            # edit record on postgresql
            new_record = get_object_or_404(Movie, pk=movie_id)
            new_record.name = payload.name
            new_record.protagonists = payload.protagonists
            new_record.start_date = payload.start_date
            new_record.status = payload.status
            new_record.ranking = payload.ranking
            new_record.poster = poster
            new_record.save()

            # edit record on mongodb
            db_edit_movie(new_record)

            return 200, {"message": "Data has successfully been Updated"}
    except:
        return 500, {"message": "Server error"}


@router.get('/movie/{int:movie_id}', response=RetrieveMovieSchema)
def get_movie(request, movie_id):

    movie_record = get_object_or_404(Movie, pk=movie_id)
    return movie_record


@router.get('/movie/all')
def get_all_movie(request):
    return db_retrieve_all_movie()


@router.post('/redis-check')
def checking(request):
    increment_ranks.delay(2, 3)
