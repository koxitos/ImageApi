from rest_framework import serializers

from ImageApi.ImageApiApp.exceptions import FileNotSupportedException
from ImageApi.ImageApiApp.models import Image


class ImageSeralizer(serializers.ModelSerializer):
    """Image serializer class."""

    id = serializers.IntegerField(read_only=True)
    url = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ['id', 'url', 'title', 'width', 'height', 'image']

    def get_url(self, instance):
        return instance.image.url

    @property
    def width(self):
        return self.validated_data.get('width', 0)

    @property
    def height(self):
        return self.validated_data.get('height') or 0

    @property
    def image(self):
        return self.validated_data.get('image')

    @property
    def title(self):
        return self.validated_data.get('title')

    @staticmethod
    def validate_file_format(image_type):
        """Validates image type."""
        for image_format in Image.SUPPORTED_FILE_FORMATS:
            if image_format.upper() in image_type.upper():
                return image_format

        raise FileNotSupportedException(
            f"Resizing '{image_type}' type is not supported."
            f"Supported file formats: {Image.SUPPORTED_FILE_FORMATS}")
