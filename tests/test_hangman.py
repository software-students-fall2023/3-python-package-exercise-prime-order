from pygamebox import Hangman

def test_get_word():
    length = 2
    hangman = Hangman()
    assert len(hangman.word) == length
    assert hangman.guesses == 0

def get_user_guess():
    hangman = Hangman()
    assert hangman.get_user_guess() == 'a'

def test_validate_input():
    hangman = Hangman()
    assert hangman.validate_input('a') == True
    assert hangman.validate_input('aa') == False
    assert hangman.validate_input('') == False

def test_check_win():
    hangman = Hangman()
    assert hangman.check_win(['a', 'a', 'a', 'a']) == True
    assert hangman.check_win(['a', 'a', '_', 'a']) == False

def test_play():
    hangman = Hangman()
    pass


