function updateWordDisplay() {
    let displayWord = '';
    for (let letter of word) {
        displayWord += guessedLetters.includes(letter) ? letter : '_';
    }
    document.getElementById('word-display').innerText = displayWord;
}

function submitGuess() {
    let letter = document.getElementById('letter-input').value.toLowerCase();
    if (!letter) return;

    fetch(`/guess/${gameId}/?letter=${letter}`)
        .then(response => response.json())
        .then(data => {
            guessedLetters += letter;
            guessCount++;
            document.getElementById('guess-count').innerText = guessCount;
            document.getElementById('message').innerText = data.message;
            updateWordDisplay();

            if (data.message === 'You win!') {
                alert('You won the game!');
            }
        });

    document.getElementById('letter-input').value = '';
}
