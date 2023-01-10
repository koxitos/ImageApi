from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from ImageApi.ImageApiApp.exceptions import FileNotSupportedException
from ImageApi.storage import get_media_storage, MediaStorage

storage = get_media_storage()


class Image(models.Model):
    """."""
    SUPPORTED_FILE_FORMATS = {'png', 'jpg', 'jpeg', 'bmp', 'gif'}

    title = models.CharField(max_length=200, blank=False)
    width = models.IntegerField(validators=[
        MaxValueValidator(1000),
        MinValueValidator(100)
        ])
    height = models.IntegerField(validators=[
        MaxValueValidator(1000),
        MinValueValidator(100)
        ])
    image = models.ImageField(
        upload_to=MediaStorage.media_storage_dir,
        storage=storage,
        blank=True,
    )

    @staticmethod
    def validate_file_type(magic_type):
        """Validates image type."""
        for image_format in Image.SUPPORTED_FILE_FORMATS:
            if image_format.upper() in magic_type.upper():
                return image_format
        raise FileNotSupportedException(
            f"Resizing '{magic_type}' type is not supported.")
