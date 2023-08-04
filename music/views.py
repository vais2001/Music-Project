from django.shortcuts import render
from django.http import HttpResponse
from music.models.listner import Song
from django.views import View
from music.models.viewer import Viewer

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



def signup(request):
    print(request.method)
    if request.method=='GET':
        return render(request,'signup.html')
    else:
        postData=request.POST
        viewer_name=postData.get('viewer_name')
        email=postData.get('email')
        password=postData.get('password')
        rearrange_password=postData.get('rearrange_password')
        print(viewer_name,email,password,rearrange_password)
         
         
        value={
            'viewer_name':viewer_name,
            'email':email
        }  
        error_message=None 
        if not viewer_name:
           error_message='name is required' 
        elif not email:
            error_message='required'
        elif len(password) <6:
            error_message='should be min 6 and above from 6'     
        if not error_message:   
            print(viewer_name,email,password)     
            viewer=Viewer(viewer_name=viewer_name,
                       email=email,
                       password=password,
                       rearrange_password=rearrange_password
                    )
            viewer.save()
            return render (request,'login.html')
        else:
            data={
                'error':error_message,
                'values':value
            }
            return render(request,'signup.html',data) 
def login(request):
      return render(request,'login.html')
    