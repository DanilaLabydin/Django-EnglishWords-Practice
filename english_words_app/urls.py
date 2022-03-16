from django.urls import path
from . import views

app_name = 'english_words_app'
urlpatterns = [
    path("", views.index, name='index'),
]
