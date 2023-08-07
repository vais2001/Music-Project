from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from music.models.listner import Song
from django.views import View
from music.models.viewer import Viewer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

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



# def signup(request):
#     print(request.method)
#     if request.method=='GET':
#         return render(request,'signup.html')
#     else:
#         postData=request.POST
#         viewer_name=postData.get('viewer_name')
#         email=postData.get('email')
#         password=postData.get('password')
#         rearrange_password=postData.get('rearrange_password')
#         print(viewer_name,email,password,rearrange_password)
         
         
#         value={
#             'viewer_name':viewer_name,
#             'email':email
#         }  
#         error_message=None 
#         if not viewer_name:
#            error_message='name is required' 
#         elif not email:
#             error_message='required'
#         elif len(password) <6:
#             error_message='should be min 6 and above from 6' 
#         elif not phone:
#             error_message='required'        
#         if not error_message:   
#             print(viewer_name,email,password)     
#             viewer=Viewer(viewer_name=viewer_name,
#                        email=email,
#                        password=password,
#                        rearrange_password=rearrange_password
#                     )
#             viewer.save()
#             return render (request,'login.html')
#         else:
#             data={
#                 'error':error_message,
#                 'values':value
#             }
#             return render(request,'signup.html',data) 
    
    
def signup(request):
    if request.method=="POST":
         user_name=request.POST.get('user_name')
         first_name=request.POST.get( ' first_name')
         last_name=request.POST.get( 'last_name')
         phone=request.POST.get( 'phone')
         email=request.POST.get( 'email')
         pass1=request.POST.get( 'pass1')
         pass2=request.POST.get( 'pass2')   
         print(user_name,first_name,last_name,phone,email,pass1,pass2)
         myuser=User.objects.create_user(user_name,email)
         print('----------------------------------')
         print(myuser.username)
         myuser.set_password(pass1)
         print(myuser)
         myuser.firstname=first_name
         myuser.lastname=last_name
         print(myuser.first_name, myuser.last_name)
         print('----------------------')
         myuser.save()
         print(user_name, pass1)
         user=authenticate(username=user_name,password=pass1) 
         print(type(user))
       
         login(request,user)
         return redirect('/')
    return render(request,'signup.html')
    

    
    
    
    
def loginpage(request):
    if request.method=="POST":
      user_name=request.POST.get('user_name') 
      pass1=request.POST.get( 'pass1')
      print(user_name, pass1)
      user=authenticate(username=user_name,password=pass1) 
      print(type(user))
     
      login(request,user)
      print(request.user)
      return redirect('/')
    else:
        
      return render(request,'login.html')
  
  
def logoutpage(request):
    logout(request)
    return HttpResponseRedirect('/login/')
    
    
def change_pass(request):
    return render(request,'changepassword')   