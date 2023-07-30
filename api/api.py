from ninja import Router, UploadedFile, File, Form
from .schema import MovieSchema
from .models import Movie

router = Router()

@router.post('/add_movie')
def add_movie(request, payload: MovieSchema = Form(...), poster: UploadedFile=File(...)):
    Movie.objects.create(**payload.dict(), poster=poster)
