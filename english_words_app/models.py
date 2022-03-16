from django.db import models


# Create your models here.
class EnglishWord(models.Model):
    word = models.TextField()
    translation = models.TextField()

    def __str__(self):
        return self.word
