from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('comments/', views.comments, name='comments'),
    path('persons/', views.persons, name='persons'),
    path('add_comment/', views.add_comment, name='add_comment'),
    path('films/', views.films, name='films'),
    path('add_film/', views.add_film, name='add_film'),
]