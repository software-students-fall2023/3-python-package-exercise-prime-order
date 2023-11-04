from pygamebox import WordScramble
from pathlib import Path

DATA_DIR = Path(__file__).parent.absolute() / "data"

def test_read_word_file():
    game = WordScramble()

    # Read words from the 'words.txt' file located in the 'data' directory
    game.all_words = game.read_word_file(DATA_DIR / 'words.txt')

    # Define test data for comparison
    test_data = ['apple', 'banana', 'orange']

    # Assert that the number of words read matches the expected count
    assert len(game.all_words) == 3

    # Assert that the words read match the test data
    assert game.all_words == test_data


def test_get_random_word():
    game = WordScramble()

    # Define a test list of words
    test_data = ['apple', 'banana', 'orange']

    # Get a random word from the test data
    word = game.get_random_word(test_data)

    # Assert that the randomly selected word is in the test data
    assert word in test_data


def test_scramble_word():
    game = WordScramble()

    # Define a test word
    test_word = 'apple'

    # Scramble the test word
    scrambled_word = game.scramble_word(test_word)

    # Assert that the length of the scrambled word is the same as the original word
    assert(len(test_word) == len(scrambled_word))

    # Assert that the set of characters in the original and scrambled words are the same
    assert(set(test_word) == set(scrambled_word))

    # Assert that the scrambled word is not the same as the original word
    assert(test_word != scrambled_word)

def test_get_word_list():
    game = WordScramble()

    # Get word lists for easy, medium, and hard difficulty levels
    
    easy_words = game.get_word_list(1)
    medium_words = game.get_word_list(2)
    hard_words = game.get_word_list(3)

    # Assert that all words in the easy list have a length less than or equal to 4
    assert all(len(word) <= 4 for word in easy_words)

    # Assert that all words in the medium list have a length between 5 and 7
    assert all(5 <= len(word) <= 7 for word in medium_words)

    # Assert that all words in the hard list have a length greater than or equal to 8
    assert all(len(word) >= 8 for word in hard_words)
