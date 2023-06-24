from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.upload, name='index'),
    path('player', views.player, name='player'),
    path('extract_subtitles/', views.extract_subtitles, name='view_video'),
    path('view_video/', views.view_video, name='view_video'),
]
