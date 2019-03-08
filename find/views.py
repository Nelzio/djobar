from django.shortcuts import render
# Download
import os
from mimetypes import guess_type
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
from django.http import FileResponse
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
    file_path = os.path.join('find', 'static', 'find', 'downloads', 'linuxmint-19.1-xfce-64bit.iso')
    '''
    with open(file_path, 'rb') as f:
        response = HttpResponse(f, content_type=guess_type(file_path)[0])
        response['Content-Length'] = len(response.content)
        return response
    '''
    filename = os.path.basename(file_path)
    # filename = "Mint"
    chunk_size = 8192
    response = FileResponse(open(file_path, 'rb'))
    '''
    response = StreamingHttpResponse(
       FileWrapper(open(file_path, 'rb'), chunk_size),
       content_type="application/octet-stream"
    )
    '''
    # response['Content-Length'] = os.path.getsize(the_file)    
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


def aaa(request):
    return render(request, 'find/index.html')
