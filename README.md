# ImageApi

how to run this?

1. Set env variable named `'IMAGE_API_REPO_DIR'` with repository location, for example:

```
export IMAGE_API_REPO_DIR="/home/user/some_dir_with_repo"
```

2. Configure s3 bucket... (out of scope here)

3. Add `.env` file in ImageApi with settings:

```
DB_NAME='imageApi'
DB_USER='imageApi'
DB_PASSWORD='imageApi'

AWS_ACCESS_KEY_ID = '<your_aws_key_id>'
AWS_SECRET_ACCESS_KEY = '<your_secret_access_key>'
AWS_STORAGE_BUCKET_NAME = 's3-md-bucket'
```

4. Go do dev and run:

```docker-compose build
cd dev
docker-compose run web migrate
docker-compose up
```

Swagger documentation should be available here:
```
http://localhost:8000/redoc/
```

