from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DocumentForm
from .models import GalleryImage
from django.http import HttpResponse, JsonResponse
from PIL import Image, ImageFilter
from django.middleware.csrf import get_token
import boto3
import json
from django.db.models.fields.files import ImageFieldFile
import os


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

def picture(request, id):   
    picture = GalleryImage.objects.get(id = id)
    csrf_token = get_token(request)
    return render(request, 'picture.html', {'picture': picture, 'csrf_token': csrf_token})

def delete(request):
    GalleryImage.objects.all().delete()
    return redirect('index')

def aws(request, id):
    picture = GalleryImage.objects.get(id = id)
    # session = boto3.Session(region_name='us-east-1')
    session = boto3.Session(region_name='us-west-2')
    rekognition = session.client('rekognition')

    # Cargar imagen
    with open(picture.image.path, 'rb') as image_file:
        image = image_file.read()
    response = rekognition.detect_faces(Image = { 'Bytes': image }, Attributes = [ 'ALL' ])
    filtered_faces = filter(lambda face: face["AgeRange"]["Low"] < 18, response['FaceDetails'])
    filtered_faces = list(map(lambda face: face['BoundingBox'], filtered_faces))
    return JsonResponse(filtered_faces, safe = False)

def blur(request, id):
    image = GalleryImage.objects.get(id = id)
    path = image.image.path
    csrf_token = get_token(request)
    img = Image.open(path)
    body = json.loads(request.body)
    coords = body.get('coords')
    for coord in coords:
        x = int(coord['x'])
        y = int(coord['y'])
        w = int(coord['w'])
        h = int(coord['h'])
        region = img.crop((x, y, x + w, y + h))
        for i in range(0, 40):
            region = region.filter(ImageFilter.BLUR)
        img.paste(region, (x, y, x + w, y + h))

    #print('IMAGE.FILE.PATH -------------------- ', path)
    extension = os.path.splitext(path)[1]
    len_extension = len(extension)

    path = path[:-len_extension] + '-blured' + path[-len_extension:]
    img.save(path)
    image.blur = ImageFieldFile(image, image.blur, path) 
    image.save()
    #print('------------------------------------------- SAVED')

    return render(request, 'picture.html', {'pic': image, 'csrf_token': csrf_token})