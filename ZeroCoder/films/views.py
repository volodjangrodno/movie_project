from django.shortcuts import render, redirect
from .models import Film_comment, Add_film
from .forms import Film_commentForm, Add_filmForm

# Create your views here.
def index(request):
    film = Add_film.objects.all()
    return render(request, 'films/index.html', {'film': film})

def comments(request):
    film_comment = Film_comment.objects.all()
    return render(request, 'films/comments.html', {'film_comment': film_comment})

def persons(request):
    return render(request, 'films/persons.html')

def add_comment(request):
    error = ''
    if request.method == 'POST':
        form = Film_commentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comments')
        else:
            error = "Данные были заполнены некорректно"
    form = Film_commentForm()
    return render(request, 'films/add_comment.html', {'form': form, 'error': error})

def films(request):
    return render(request, 'films/films.html')

def add_film(request):
    film_error = ''
    if request.method == 'POST':
        film_form = Add_filmForm(request.POST, request.FILES)
        if film_form.is_valid():
            film_form.save()
            return redirect('')
        else:
            film_error = "Данные были заполнены некорректно"
    film_form = Add_filmForm()
    return render(request, 'films/add_film.html', {'film_form': film_form}, {'film_error': film_error})
