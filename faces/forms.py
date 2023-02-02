from django import forms
from .models import GalleryImage

class DocumentForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['file']