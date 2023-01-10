import django_filters

from ImageApi.ImageApiApp.models import Image


class ImageFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Image
        fields = ['title']
