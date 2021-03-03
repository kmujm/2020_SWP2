class Guess:

    def __init__(self, word):
        self.secretWord = word
        self.numTries = 0
        self.guessedChars = set()
        self.currentStatus = ['_']*len(self.secretWord)

    def displayCurrent(self):
        guessWord = ''
        for c in self.currentStatus:
            guessWord += (c + ' ')
        return guessWord

    def displayGuessed(self):
        return ' ' + ' '.join(sorted(list(self.guessedChars)))

    def guess(self, character):
        self.guessedChars |= {character}
        if character not in self.secretWord:
            return False
        idx = self.secretWord.find(character)
        while idx != -1:
            self.currentStatus[idx] = character
            idx = self.secretWord[idx + 1:].find(character)

        return True

    def finished(self):
            return True if "".join(self.currentStatus) == self.secretWord else False
