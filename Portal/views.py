from django.shortcuts import render
from django.template.response import TemplateResponse

# Create your views here.
def index(request):
    if request.method == 'GET':
        context = {
            'message': "Hello, world!",
        }
        return  TemplateResponse(request, 'index.html', context)

