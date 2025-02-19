from django.shortcuts import render  
from django.http import JsonResponse
from .models import WordGame
import random

# Predefined list of words
words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']

def get_random_word():
    """Helper function to get a random word from the list"""
    return random.choice(words)

def index(request):
    """Render the main game page"""
    word = get_random_word()  
    game = ç.objects.create(word=word) 
    return render(request, 'index.html', {'game_id': game.id, 'word': word})

def guess_letter(request, game_id):
    """Process a letter guess"""
    game = WordGame.objects.get(id=game_id)
    letter = request.GET.get('letter', '').lower()

    if letter in game.word and letter not in game.guessed_letters:
        game.guessed_letters += letter
        game.correct_guesses += 1
    elif letter not in game.word and letter not in game.guessed_letters:
        game.guessed_letters += letter  

    game.total_guesses += 1
    game.save()

    updated_word = ''.join([char if char in game.guessed_letters else '_' for char in game.word])

    if game.correct_guesses == len(set(game.word)):
        # Reset the game with a new word after winning
        new_word = get_random_word()
        game.word = new_word
        game.guessed_letters = ""
        game.correct_guesses = 0
        game.total_guesses = 0
        game.save()
        
        return JsonResponse({'message': 'You win!', 'word': updated_word, 'guesses': game.total_guesses, 'new_word': new_word})

    return JsonResponse({'message': 'Correct guess!' if letter in game.word else 'Wrong guess, try again!', 'word': updated_word, 'guesses': game.total_guesses})
