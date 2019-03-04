from django.shortcuts import render

# Create your views here.


def home(request):
    data = {}
    data['test'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 3, 4, 5, 6, 78, 9, 9, 5]
    return render(request, 'find/index.html', data)
