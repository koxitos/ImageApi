from rest_framework import filters
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework import viewsets
from ImageApi.ImageApiApp.filters import ImageFilter
from ImageApi.ImageApiApp.models import Image
from ImageApi.ImageApiApp.serializers import ImageSeralizer

from rest_framework import status
from rest_framework.response import Response
from ImageApi.ImageApiApp import utils
from drf_yasg.utils import swagger_auto_schema


class ImageView(viewsets.ModelViewSet):
    """Image viewset."""
    serializer_class = ImageSeralizer
    queryset = Image.objects.all()
    parser_classes = [MultiPartParser]
    filterset_class = ImageFilter

    @swagger_auto_schema()
    def create(self, request):
        serializer = ImageSeralizer(data=request.data)
        serializer.is_valid(raise_exception=True)

        title = serializer.title
        image = serializer.image
        width = serializer.width
        height = serializer.height

        file_type = utils.get_image_file_type(image=image)
        ImageSeralizer.validate_file_format(file_type)
        image.name = f"{title}.{file_type}"[:200] if title else image.name
        image.file = utils.resize_image(image_file=image.file,
                                        width=width,
                                        height=height,
                                        file_type=file_type)

        serializer.save(image=image, width=width, height=height, title=title)
        return Response(status=status.HTTP_201_CREATED)
