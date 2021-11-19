from django import forms
from testapp.models import Category,Photo

class PhotoForm (forms.ModelForm):
    class Meta :
        model = Photo
        fields = '__all__'
