from django.db import models

class WordGame(models.Model):
    word = models.CharField(max_length=100)
    guessed_letters = models.CharField(max_length=100, blank=True)
    correct_guesses = models.IntegerField(default=0)
    total_guesses = models.IntegerField(default=0)

    def __str__(self):
        return self.word
