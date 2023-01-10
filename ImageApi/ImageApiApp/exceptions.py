from rest_framework import serializers


class FileNotSupportedException(serializers.ValidationError):
    """Exception raised for not supported file type."""
    pass
