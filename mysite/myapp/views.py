from django.shortcuts import render
from django.http.response import HttpResponse

def index_template(request):
    return render(request, 'index.html')


# Create your views here.
