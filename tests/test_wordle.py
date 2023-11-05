from pygamebox import Wordle
from pathlib import Path

DIR = Path(__file__).parent.absolute() / "data"
def test_init():
    wordle = Wordle()
    assert wordle.guesses == 0
    assert wordle.words == []

def test_validate_input():
    wordle = Wordle()
    word = wordle.get_word( DIR / 'words.txt')
    # test input that the word is correctly returned
    test = ['apple','banana','orange']
    #assert that the word is correctly returned
    assert word in test
    #assert that the word not in the test list is false
    assert wordle.validate_input('a') == False
    assert wordle.validate_input(' ') == False

def test_check_win():
    wordle = Wordle()
    wordle.word = 'test'
    assert wordle.check_win('test') == True
    assert wordle.check_win('testt') == False
