from django.contrib import admin
from django.urls import path
from music import views
urlpatterns = [
    path('',views.index),
    path('song',views.song_list,name='song'),
    path('listen_song',views.listen,name='listen_song')
]
