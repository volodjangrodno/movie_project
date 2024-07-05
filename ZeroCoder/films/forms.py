from .models import Film_comment
from .models import Add_film
from django.forms import ModelForm, TextInput, Textarea, FileInput

class Film_commentForm(ModelForm):
    class Meta:
        model = Film_comment
        fields = ['title', 'description', 'comment']
        widjets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название фильма'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание фильма'}),
            'comment': Textarea(attrs={'class': 'form-control', 'placeholder': 'Комментарий к фильму'}),
        }

class Add_filmForm(ModelForm):
    class Meta:
        model = Add_film
        fields = ['film_title', 'film_description', 'image']
        widjets = {
            'film_title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название фильма'}),
            'film_description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание фильма'}),
            'image': FileInput(attrs={'class': 'form-control', 'placeholder': 'Изображение'}),
        }