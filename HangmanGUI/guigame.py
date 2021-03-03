from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QTextEdit
from PyQt5.QtWidgets import QLineEdit, QToolButton

from word import Word
from hangman import Hangman
from guess import Guess
from PyQt5.QtCore import Qt

class HangmanGame(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.word = Word('words.txt')

        hangmanLayout = QGridLayout()

        self.hangmanWindow = QTextEdit()
        self.hangmanWindow.setReadOnly(True)
        self.hangmanWindow.setAlignment(Qt.AlignLeft)
        font = self.hangmanWindow.font()
        font.setFamily('Courier New')
        self.hangmanWindow.setFont(font)
        hangmanLayout.addWidget(self.hangmanWindow, 0, 0)

        statusLayout = QGridLayout()

        self.currentWord = QLineEdit()
        self.currentWord.setReadOnly(True)
        self.currentWord.setAlignment(Qt.AlignCenter)
        font = self.currentWord.font()
        font.setPointSize(font.pointSize() + 8)
        self.currentWord.setFont(font)
        statusLayout.addWidget(self.currentWord, 0, 0, 1, 2)

        self.guessedChars = QLineEdit()
        self.guessedChars.setReadOnly(True)
        self.guessedChars.setAlignment(Qt.AlignCenter)
        self.guessedChars.setMaxLength(52)
        statusLayout.addWidget(self.guessedChars, 1, 0, 1, 2)

        self.message = QLineEdit()
        self.message.setReadOnly(True)
        self.message.setAlignment(Qt.AlignCenter)
        self.message.setMaxLength(52)
        statusLayout.addWidget(self.message, 2, 0, 1, 2)

        self.charInput = QLineEdit()
        self.charInput.setMaxLength(1)
        statusLayout.addWidget(self.charInput, 3, 0)

        # Button for submitting a character
        self.guessButton = QToolButton()
        self.guessButton.setText('Guess!')
        self.guessButton.clicked.connect(self.guessClicked)
        statusLayout.addWidget(self.guessButton, 3, 1)

        # Button for a new game
        self.newGameButton = QToolButton()
        self.newGameButton.setText('New Game')
        self.newGameButton.clicked.connect(self.startGame)
        statusLayout.addWidget(self.newGameButton, 4, 0)

        mainLayout = QGridLayout()
        mainLayout.addLayout(hangmanLayout, 0, 0)
        mainLayout.addLayout(statusLayout, 0, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle('HangmanGame')

    def startGame(self):
        self.hangman = Hangman()
        self.guess = Guess(self.word.randFromDB(5))
        if 9 < len(self.guess.secretWord):
            self.currentWord.setFixedWidth(300)

        self.hangmanWindow.setPlaceholderText(self.hangman.currentShape())
        self.currentWord.setText(self.guess.displayCurrent())
        self.guessedChars.setText(self.guess.displayGuessed())
        self.message.clear()

    def guessClicked(self):
        guessedChar = self.charInput.text()
        self.charInput.clear()
        self.message.clear()

        if not guessedChar.isalpha():
            self.message.setText('Please input alphabet!')
            return

        if self.guess.finished():
            self.message.setText('GAME OVER!')
            return

        if len(guessedChar) != 1:
            self.message.setText('Please input one letter')
            return

        if guessedChar in self.guess.guessedChars:
            self.message.setText('You already guessed \"' + guessedChar + '\"')
            return

        if not self.guess.guess(guessedChar):
            self.hangman.decreaseLife()
            self.message.setText('Fail!')
        else:
            self.message.setText('Success!')

        self.hangmanWindow.setPlaceholderText(self.hangman.currentShape())
        self.currentWord.setText(self.guess.displayCurrent())
        self.guessedChars.setText(self.guess.displayGuessed())

        if self.guess.finished():
            self.message.setText('You Win!')
        elif self.hangman.getRemainingLives() == 0:
            self.message.setText('You Lose! Secret word was ' + self.guess.secretWord +'.')
        if self.guess.finished() or self.hangman.getRemainingLives() == 0:
            self.charInput.setDisabled(True)
            self.guessButton.setDisabled(True)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    game = HangmanGame()
    game.show()

    sys.exit(app.exec_())
