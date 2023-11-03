from pygamebox import GuessTheNumber

def test_random_number_init():
    game = GuessTheNumber(start=11, end=23)

    # check that number is an integer
    assert isinstance(game.number, int)

    # check that number generated is within range
    assert game.number >= game.start and game.number <= game.end

def test_validate_input():
    game = GuessTheNumber(start=1, end=100)

    # in range values
    assert game.validate_input(50) == True

    # out of range values
    assert game.validate_input(-100) == False
    assert game.validate_input(200) == False

    # non-numeric values
    assert game.validate_input("50") == True
    assert game.validate_input("hello") == False
    assert game.validate_input([34, 123, 12]) == False

def test_guess():
    game = GuessTheNumber(start=1, end=100)
    game.number = 50

    # lower than number
    assert game.guess(1) == -1

    # higher than number
    assert game.guess(100) == 1

    # equal to number
    assert game.guess(50) == 0

def test_turn():
    game = GuessTheNumber(start=1, end=100)
    game.number = 50

    # wrong guess should not terminate game
    assert game.turn(1) == False
    # guesses counter should increment
    assert game.guesses == 1

    assert game.turn(100) == False
    assert game.guesses == 2

    # correct guess should terminate game
    assert game.turn(50) == True
    assert game.guesses == 3

    # reset should reset guesses counter
    game.reset()
    assert game.guesses == 0
