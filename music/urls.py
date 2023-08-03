from django.contrib import admin
from django.urls import path
from music import views
urlpatterns = [
    path('',views.index),
    path('song',views.song_list,name='song'),
    path('listen_song/<int:id>',views.listen,name='listen_song'),
    path('signup',views.sign_up,name='signup')
]
