from django.shortcuts import render
from django.views.generic import ListView
from .models import EnglishWord


def index(request):
    words = EnglishWord.objects.order_by('word')
    context = {'posts': words}
    return render(request, 'english_words_app/index.html', {'words': words})
