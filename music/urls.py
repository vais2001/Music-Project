from django.contrib import admin
from django.urls import path
from music import views
# from .views import Sign_up
urlpatterns = [
    path('',views.index,name='index'),
    path('song',views.song_list,name='song'),
    path('listen_song/<int:id>',views.listen,name='listen_song'),
    # path('signup/',Sign_up.as_view(),name='signup'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.loginpage,name='login'),
    path('logout/',views.logoutpage,name='logout'),
    path('changepassword/',views.change_pass,name='changepassword'),
    path('watchlater/',views.watchlater,name='watchlater')
    
]
