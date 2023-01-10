from ImageApi import settings
from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    bucket_name = 's3-md-bucket'
    media_storage_dir = f'test'
    media_storage_base_url = f'https://{bucket_name}.s3.amazonaws.com/{media_storage_dir}'


def get_media_storage():
    # if settings.UPLOADS_USE_S3:
    media_storage = MediaStorage()
    # else:
    #    media_storage = LocalMediaStorage()
    return media_storage

#def get_base_url():
