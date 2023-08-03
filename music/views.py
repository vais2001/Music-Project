from django.shortcuts import render
from django.http import HttpResponse
from music.models.listner import Song

# Create your views here.
def index(request):
    song=Song.objects.all()
    return render(request,'index.html',{'song':song})



def song_list(request):
    song=Song.objects.all()
    return render(request,'song.html',{'song':song})


# def listen(song_id):
#     print(Song.objects.filter(songid=song_id))
def listen(request,id):
    song=Song.objects.filter(song_id=id).first()
    print(song.song_name)
    return render(request,'listen.html',{'song':song})


def sign_up(request):
    return render(request,'signup.html')