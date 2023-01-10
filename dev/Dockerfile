FROM python

RUN apt update & \
    apt install -y libpq-dev

WORKDIR /code

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install django gunicorn psycopg2-binary dj-database-url

WORKDIR /application
COPY entrypoint.sh .
RUN ["chmod", "+x", "/application/entrypoint.sh"]

ENTRYPOINT ["/application/entrypoint.sh"]
