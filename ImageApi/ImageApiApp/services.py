from ImageApi.ImageApiApp.exceptions import FileNotSupportedException
from ImageApi.ImageApiApp.models import Image
from ImageApi.ImageApiApp import utils
from ImageApi.storage import MediaStorage


class ImageService:

    @staticmethod
    def _get_supported_file_format(magic_type):
        """Validates image type."""
        for image_format in Image.SUPPORTED_FILE_FORMATS:
            if image_format.upper() in magic_type.upper():
                return image_format

        raise FileNotSupportedException(
            f"Resizing '{magic_type}' type is not supported.")

    @staticmethod
    def create_image(image, width: int, height: int, title: str) -> Image:
        """Upload image main logic"""

        file_type = utils.get_image_file_type(image=image)
        image.name = f"{title}.{file_type}" if title else image.name
        image.file = utils.resize_image(image_file=image.file,
                                  width=width,
                                  height=height,
                                  file_type=file_type)

        image = Image(image=image, height=height, width=width)
        image.save()

        return image
