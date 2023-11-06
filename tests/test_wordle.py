from pygamebox import Wordle

def test_get_word_list():
    game = Wordle()

    # Assert that words_list returns a list of words
    assert isinstance(game.words_list, list)
    
    # Assert that self.words_list contains words
    assert len(game.words_list) > 0

    # Assert that a word is returned
    assert isinstance(game.word, str)

    # Assert that words is an empty list at first.
    assert game.words == []

    # Assert that guesses is 0 at first.
    assert game.guesses == 0

def test_validate_input():
    game = Wordle()
    # Assert that validate_input returns true for words of the correct length
    assert game.validate_input('apple') == True
    # Assert that validate_input returns false for words of the incorrect length
    assert game.validate_input(' ') == False
    assert game.validate_input('apples') == False
    

def test_win():
    game = Wordle()
    # dummy variable for testing
    game.word = 'apple'
    # Assert check_win returns true for correct words.
    assert game.check_win('apple') == True
    # Assert check_win returns false for incorrect words.
    assert game.check_win('orange') == False
