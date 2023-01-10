from PIL import Image
from io import BytesIO


def resize_image(image_file, width, height, file_type="PNG"):
    """Resize given image to width and height and saves to given format."""
    new_image = Image.open(image_file)
    new_image = new_image.resize((width, height))
    bytes_io = BytesIO()
    new_image.save(bytes_io, format=file_type.upper())
    return bytes_io


def get_image_file_type(image):
    """."""
    return Image.open(image.file).format
