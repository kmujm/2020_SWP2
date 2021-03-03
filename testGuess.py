import unittest

from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        self.g1.guess('e')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('k')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')  #secretWord에 없는 알파벳 입력시

    def testDisplayGuessed(self):
        self.g1.guess('e')
        self.g1.guess('n')
        self.assertEqual(self.g1.displayGuessed(), ' e n')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u')

    def testguess(self):
        self.g1.guess('k')
        self.assertEqual(self.g1.guess('k'), False)
        self.assertEqual(self.g1.currentStatus, ['_', '_', '_', '_', '_', '_', '_'])
        self.assertEqual(self.g1.guessedChars, {'k'})
        self.g1.guess('a')
        self.assertEqual(self.g1.guess('a'), True)
        self.assertEqual(self.g1.currentStatus, ['_', '_', '_', 'a', '_', '_', '_'])
        self.assertEqual(self.g1.guessedChars, {'k', 'a'})
        self.g1.guess('d')
        self.assertEqual(self.g1.guess('d'), True)
        self.assertEqual(self.g1.currentStatus, ['d', '_', '_', 'a', '_', '_', '_'])
        self.assertEqual(self.g1.guessedChars, {'k', 'a' ,'d'})

    def testfinished(self):
        self.g1.guess('e')
        self.g1.guess('d')
        self.assertEqual(self.g1.currentStatus, ['d', 'e', '_', '_', '_', '_', '_'])
        self.assertEqual(self.g1.finished(), False)
        self.g1.guess('f')
        self.assertEqual(self.g1.finished(), False)
        self.g1.guess('a')
        self.assertEqual(self.g1.finished(), False)
        self.g1.guess('u')
        self.assertEqual(self.g1.finished(), False)
        self.g1.guess('l')
        self.assertEqual(self.g1.finished(), False)
        self.assertEqual(self.g1.currentStatus, ['d', 'e', 'f', 'a', 'u', 'l', '_'])
        self.g1.guess('t')
        self.assertEqual(self.g1.finished(), True)


if __name__ == '__main__':
    unittest.main()

