from django.http import HttpResponse, Http404
# from django.template import loader
from django.shortcuts import render
from .models import Album

def index(request):
    all_albums = Album.objects.all()
    # template = loader.get_template('music/index.html')
    context = {"all_albums": all_albums }
    return render(request, 'music/index.html', context)

def detail(request, pk):
    try:
        album = Album.objects.get(pk=pk)
        context = {"album": album}
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request, 'music/detail.html', context)
