# Instuct on what image we want to base our container 
FROM python:3.10.9-alpine3.16

# Allows docker to cache installed dependencies between builds
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Mounts the application code to the image
# Instruct the copy run command in the path
WORKDIR /Movies
COPY ./api /Movies/api
COPY ./Movies /Movies/Movies
COPY ./tests /Movies/tests
COPY manage.py /Movies/
COPY README.md /Movies/


# Instruct the container where to listen to
EXPOSE 8000

#runs the production server
# ENTRYPOINT [ "python3"]
# CMD [ "manage.py", "runserver", "0.0.0.0:8000" ]


