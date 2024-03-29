from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gallery', views.gallery,  name='gallery'),
    path('picture/<int:id>', views.picture, name='picture'),
    path('delete', views.delete, name='delete'),
    path('aws/<int:id>', views.aws, name='aws'),
    path('blur/<int:id>', views.blur, name='blur')
]