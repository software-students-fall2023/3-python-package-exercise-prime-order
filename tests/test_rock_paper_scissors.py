from pygamebox import RockPaperScissors

def test_validate_input():
    game = RockPaperScissors()

    assert game.validate_input(1) == True  # 1 is a valid choice
    assert game.validate_input(2) == True  # 2 is a valid choice
    assert game.validate_input(3) == True  # 3 is a valid choice

    assert game.validate_input('1') == True  # '1' is a valid choice
    assert game.validate_input('2') == True  # '2' is a valid choice
    assert game.validate_input('3') == True  # '3' is a valid choice

    # Invalid input tests

    assert game.validate_input(0) == False  # 0 is not a valid choice
    assert game.validate_input(4) == False  # 4 is not a valid choice
    assert game.validate_input('a') == False  # 'a' is not a valid choice

def test_throw():
    game = RockPaperScissors()

    # Ensure the throw method returns an integer between 1 and 3

    assert isinstance(game.throw(), int)
    assert 0 <= game.throw() <= 2

def test_round():
    game = RockPaperScissors()

    # Tests for different game scenarios

    assert game.round(user_throw=0, computer_throw=0) == 0  # Draw
    assert game.round(user_throw=0, computer_throw=1) == -1  # Computer wins
    assert game.round(user_throw=0, computer_throw=2) == 1   # Player wins

    assert game.round(user_throw=1, computer_throw=0) == 1   # Player wins
    assert game.round(user_throw=1, computer_throw=1) == 0   # Draw
    assert game.round(user_throw=1, computer_throw=2) == -1  # Computer wins

    assert game.round(user_throw=2, computer_throw=0) == -1  # Computer wins
    assert game.round(user_throw=2, computer_throw=1) == 1   # Player wins
    assert game.round(user_throw=2, computer_throw=2) == 0   # Draw

def test_validate_round_input():
    game = RockPaperScissors()

    # Valid round input tests

    assert game.validate_round_input(1) == True  # 1 is valid
    assert game.validate_round_input(10) == True  # 10 is valid

    # Invalid round input tests

    assert game.validate_round_input(0) == False  # Non-Positive values are not valid
    assert game.validate_round_input(-10) == False
    assert game.validate_round_input('10') == False  # String input not valid