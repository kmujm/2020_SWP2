from hangman import Hangman
from guess import Guess
from word import Word


def gameMain():
    word = Word('words.txt')
    guess = Guess(word.randFromDB())
    hangman = Hangman()

    while hangman.getRemainingLives() > 0:

        display = hangman.currentShape()
        print(display)
        display = guess.displayCurrent()
        print('Current: ' + display)
        display = guess.displayGuessed()
        print('Already Used: ' + display)

        guessedChar = input('Select a letter: ')
        if len(guessedChar) != 1:
            print('One character at a time!')
            continue
        if not guessedChar.isalpha():
            print('Please input alphabet!')
            continue
        if guessedChar in guess.guessedChars:
            print('You already guessed \"' + guessedChar + '\"')
            continue

        success = guess.guess(guessedChar)
        if success == False:
            hangman.decreaseLife()

        if guess.finished():
            break

    if guess.finished() == True:
        print('**** ' + guess.displayCurrent() + ' ****')
        print('Success')
    else:
        print(hangman.currentShape())
        print('word [' + guess.secretWord + ']')
        print('guess [' + "".join(guess.currentStatus) + ']')
        print('Fail')


if __name__ == '__main__':
    gameMain()
