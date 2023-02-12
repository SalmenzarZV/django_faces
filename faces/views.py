from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DocumentForm
from .models import GalleryImage
from django.http import HttpResponse, JsonResponse
from PIL import Image, ImageFilter

def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            object = form.save()
        
        return redirect('gallery')
    else:
        pics = GalleryImage.objects.all()
        context = {
            'pics': pics
        }
        form = DocumentForm()
    return render(request, 'index.html', {'form': form, 'context': context})

def gallery(request):
    pics = GalleryImage.objects.all()
    return render(request, 'gallery.html', {'context': pics})