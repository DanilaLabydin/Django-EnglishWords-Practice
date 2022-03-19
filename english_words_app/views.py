from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, UpdateView
from .models import EnglishWord
from .forms import WordForm, WordPracticeForm


def dictionary_asc(request):
    words = EnglishWord.objects.order_by('word')
    context = {'posts': words}
    return render(request, 'english_words_app/index.html', {'words': words})


def dictionary_desc(request):
    words = EnglishWord.objects.order_by('-word')
    context = {'posts': words}
    return render(request, 'english_words_app/index.html', {'words': words})


def new_word(request):
    if request.method != 'POST':
        form = WordForm()
    else:
        form = WordForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data['word'])
            form.save()
            return redirect('english_words_app:dictionary')
    return render(request, 'english_words_app/new_word.html', {'form': form})


def words_practice(request):
    words = EnglishWord.objects.all()
    if request.method != 'POST':
        form = WordForm()
    else:
        form = WordForm(data=request.POST)
        if form.is_valid():
            return redirect('english_words_app:dictionary')
    return render(request, 'english_words_app/words_practice.html', {'words': words, 'form': form})


def words_practice1(request, word_id):
    words = EnglishWord.objects.all()

    if request.method != 'POST':
        form = WordPracticeForm()
    else:
        form = WordForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data['translation'])
            form.save()
    return render(request, 'english_words_app/words_practice1.html', {'words': words, 'form': form})


def test_fun(request, word_id):
    word = EnglishWord.objects.get(id=word_id)

    if request.method != 'POST':
        form = WordPracticeForm()
    else:
        form = WordForm(data=request.POST)
        if form.is_valid():
            form.save()
            # return redirect('english_words_app:dictionary')
    context = {'word': word, 'form': form}
    return render(request, 'english_words_app/test.html', context)


class WordUpdate(UpdateView):
    model = EnglishWord
    fields = ['translation']

    def get_context_data(self, **kwargs):
        context = super(WordUpdate, self).get_context_data()
        return context

    def get_success_url(self):
        return reverse('dictionary')

"""
class WorldUpdate(UpdateView):
    model = ToDoItem
    fields = [
        'todo_list',
        'title',
        'description',
        'due_time',
    ]

    def get_context_data(self, **kwargs):
        context = super(ItemUpdate, self).get_context_data()
        context['todo_list'] = self.object.todo_list
        context['title'] = 'Edit item'
        return context

    def get_success_url(self):
        return reverse('list', args=[self.object.todo_list_id])


def words_practice1(request):
    words = EnglishWord.objects.all()
    for word in words:
        if request.method != 'POST':
            form = WordPracticeForm()
        else:
            form = WordForm(data=request.POST)
            if form.is_valid():
                if word.word == form.cleaned_data['translation']:
                    print('yes')
                    form.save()
                else:
                    print('no')

    return render(request, 'english_words_app/words_practice1.html', {'words': words, 'form': form})
"""