from django.shortcuts import render
# Download
import os
from mimetypes import guess_type
from django.http import HttpResponse
# download
# Create your views here.


def home(request):
    data = {}
    data['test'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 3, 4, 5, 6, 78, 9, 9, 5]
    return render(request, 'find/index.html', data)


def details(request):
    return render(request, 'find/details.html')


def fonts(request):
    return render(request, 'find/fonts.html')


def download_view(request):
    file_path = os.path.join('find', 'static', 'find', 'libs', 'jquery.js.zip')

    with open(file_path, 'rb') as f:
        response = HttpResponse(f, content_type=guess_type(file_path)[0])
        response['Content-Length'] = len(response.content)
        return response


def aaa(request):
    return render(request, 'find/index.html')
