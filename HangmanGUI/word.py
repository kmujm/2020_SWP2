import random

class Word:

    def __init__(self, filename):
        self.words = []
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        for line in lines:
            word = line.rstrip()
            self.words.append(word)
        self.maxLength = len(max(self.words, key = len))

        print('%d words in DB' % len(self.words))


    def test(self):
        return 'default'


    def randFromDB(self, minLength):
        selected = False
        if minLength > self.maxLength : minLength = self.maxLength

        while not selected:
            r = random.randrange(len(self.words))
            if len(self.words[r]) > minLength:
                selected = True
        return self.words[r]
