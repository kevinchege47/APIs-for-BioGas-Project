FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED 1
RUN mkdir /backend
WORKDIR /backend
COPY requirements.txt /backend/
RUN apt-get update \
    && apt-get -y install libpq-dev gcc curl
RUN python3 -m pip install -r requirements.txt
COPY . /backend/

EXPOSE 8000

COPY entrypoint.sh .
RUN sed -i 's/\r$//g' /backend/entrypoint.sh
RUN chmod +x /backend/entrypoint.sh
# run entrypoint.sh
ENTRYPOINT ["gunicorn", "Project.wsgi", "--bind", ":8000"]