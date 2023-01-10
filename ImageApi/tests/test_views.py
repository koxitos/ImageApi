from io import BytesIO
from django.core.files.storage import Storage
from django.core.files.images import ImageFile
from django.test import Client
from mock.mock import MagicMock
from rest_framework.reverse import reverse
from PIL import Image as PilImage, ImageDraw
from ImageApi.ImageApiApp.models import Image

import pytest


def mock_images_storage():
    """Mock storage to not send images to s3."""

    def generate_filename(filename):
        return filename

    def save(name, content, max_length):
        return name

    storage_mock = MagicMock(spec=Storage, name='StorageMock')
    storage_mock.generate_filename = generate_filename
    storage_mock.save = MagicMock(side_effect=save)
    storage_mock.url = MagicMock(name='url')
    storage_mock.url.return_value = 'http://example.com/generated_filename.png'

    Image._meta.get_field('image').storage = storage_mock


def generate_image_file():
    """Util method to generate image file object."""
    image = PilImage.new('RGBA', size=(250, 250), color=(128, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.rectangle([(0, 0), image.size], fill=(200, 200, 200))
    image_file = BytesIO()
    image.save(image_file, format='PNG')  # or whatever format you prefer
    image_file.name = "some_name.png"
    return ImageFile(image_file)


def generate_image(id, title='title', width=200, height=200, image=None):
    """Helper function for generating object in db."""
    image = image or generate_image_file()
    Image(id=id,
          title=title,
          image=image,
          width=width,
          height=height) \
        .save()


@pytest.fixture
def db(django_db_blocker):
    """Generate Images object in db."""
    django_db_blocker.unblock()
    generate_image(id=0, title="image1")
    generate_image(id=1, title="image2")
    generate_image(id=2, title="image3")


def create_image_data(title="some_title", width=200, height=400):
    """Helper function to generate post data."""
    image = generate_image_file()
    image.file.seek(0)  # does not work without it!
    return {
        "title": title,
        "width": width,
        "height": height,
        "image": image.file
    }


@pytest.mark.django_db
class TestImageView:
    """ImageView test cases."""

    def setup_class(self):
        """Setup."""
        mock_images_storage()
        self.client = Client()

    def test_listing_images(self, db):
        """Test to assure that api returns images from db."""
        url = reverse("images-list")
        response = self.client.get(url)
        assert response.status_code == 200
        results = response.data['results']
        assert len(results) == 3
        image1 = results[0]
        image2 = results[1]
        image3 = results[2]

        assert image1['id'] == 0
        assert image2['id'] == 1
        assert image3['id'] == 2

        assert image1['title'] == 'image1'
        assert image2['title'] == 'image2'
        assert image3['title'] == 'image3'

    def test_listing_images_with_search(self, db):
        """Test to assure that api returns searched image by title."""
        search_by_title = "image3"
        url = f"{reverse('images-list')}?title={search_by_title}"
        response = self.client.get(url)
        assert response.status_code == 200
        results = response.data['results']
        assert len(results) == 1
        image = results[0]
        assert image['id'] == 2
        assert image['title'] == 'image3'

    def test_upload_image(self):
        """Assure that image object is created in db."""
        url = reverse('images-list')
        data = create_image_data()
        response = self.client.post(url, data=data)
        assert response.status_code == 201

    def test_upload_image_no_title(self):
        """Assure that title is required field."""
        url = reverse('images-list')
        data = create_image_data()
        data['title'] = ""
        response = self.client.post(url, data=data)
        assert response.status_code == 400

    def test_upload_image_width_validators(self):
        """Assure that width is required field."""
        url = reverse('images-list')
        data = create_image_data()
        del data['width']
        response = self.client.post(url, data=data)
        assert response.status_code == 400

    def test_upload_image_height_validators(self):
        """Assure that height is required field."""
        url = reverse('images-list')
        data = create_image_data()
        del data['height']
        response = self.client.post(url, data=data)
        assert response.status_code == 400

    def test_upload_image_file_type_validator(self):
        """Assure only certain extension types are valid."""
        url = reverse('images-list')
        data = create_image_data()
        data['image'].name = "some_nname.asd"
        response = self.client.post(url, data=data)
        assert response.status_code == 400
        assert "File extension" in response.data['image'][0]
        assert "is not allowed" in response.data['image'][0]
