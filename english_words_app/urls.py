from django.urls import path
from . import views

app_name = 'english_words_app'
urlpatterns = [
    path("", views.dictionary_asc, name='dictionary'),
    path("dictionary_desc/", views.dictionary_desc, name='dictionary_desc'),
    path("new_word/", views.new_word, name='new_word'),
    path('words_practice/', views.words_practice, name='words_practice'),
    path('words_practice1/', views.words_practice1, name='words_practice1'),
    path('test_func/<int:word_id>/', views.test_fun, name='test_func'),
]
