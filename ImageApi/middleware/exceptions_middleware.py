
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template.exceptions import TemplateDoesNotExist

class ExceptionMiddleware:
    """Exception middleware to handle some exceptions
    with no 500 error."""
    
    def __init__(self, get_response) -> None:
        """."""
        self.get_response = get_response
    
    def __call__(self, request):
        """."""
        response = self.get_response(request)
        return response
        
    def process_exception(self, request, exception):
        """."""
        if isinstance(exception, TemplateDoesNotExist):
            swagger_docs_url = reverse('schema-redoc')
            return HttpResponseRedirect(swagger_docs_url)