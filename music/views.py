# from django.http import HttpResponse, Http404
# from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Album, Song

def index(request):
    all_albums = Album.objects.all()
    # template = loader.get_template('music/index.html')
    context = {"all_albums": all_albums }
    return render(request, 'music/index.html', context)

def detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    context = {"album": album}
    # try:
    #     album = Album.objects.get(pk=pk)
    #     
    # except Album.DoesNotExist:
    #     raise Http404("Album does not exist")
    return render(request, 'music/detail.html', context)

def favorite(request, pk):
    album = get_object_or_404(Album, pk=pk)
    try:
        selected_song = album.song_set.get(pk=request.POST["song"])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {"album": album, "error_message": "you did not select a valid song"})
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', {"album": album})