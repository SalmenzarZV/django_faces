from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gallery', views.gallery,  name='gallery'),
    path('picture/<int:id>', views.picture, name='picture'),
]