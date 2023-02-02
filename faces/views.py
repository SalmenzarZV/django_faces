from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DocumentForm
from .models import GalleryImage
from django.http import HttpResponse, JsonResponse

def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            object = form.save()
        
        return redirect('gallery')
    return render(request, 'index.html', {'form': form})

def gallery(request):
    return render(request, 'gallery.html')