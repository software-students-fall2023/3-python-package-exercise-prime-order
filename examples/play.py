from pygamebox import GuessTheNumber, RockPaperScissors, WordScramble, Hangman, Wordle


def get_input(prompt: str, default: str, cast: type = int):
    user_input = input(prompt + f' (Press ENTER for default value {default}): ').strip()
    if user_input:
        return cast(user_input)
    return default


def guess_the_number():
    print('\nWelcome to Guess the Number!')
    start = get_input('Enter a lower bound', GuessTheNumber.DEFAULT_START)
    end = get_input('Enter an upper bound', GuessTheNumber.DEFAULT_END)

    game = GuessTheNumber(start=start, end=end)
    game.play()


def rock_paper_scissors():
    print('\nWelcome to Rock Paper Scissors!')
    rounds = get_input('Enter the number of rounds', RockPaperScissors.DEFAULT_ROUNDS)

    game = RockPaperScissors()
    game.play(rounds=rounds)


def word_scramble():
    print('\nWelcome to Word Scramble!')
    difficulty = get_input('Enter the difficulty level (easy, medium, hard)', WordScramble.DEFAULT_DIFFICULTY, str)
    attempts = get_input('Enter the number of attempts', WordScramble.DEFAULT_ATTEMPTS)

    game = WordScramble()
    game.play(difficulty=difficulty, attempts=attempts)


def hangman():
    print('\nWelcome to Hangman!')
    difficulty = get_input('Enter the difficulty level (easy, medium, hard)', Hangman.DEFAULT_DIFFICULTY, str)
    attempts = get_input('Enter the number of attempts', Hangman.DEFAULT_ATTEMPTS)

    game = Hangman()
    game.play(difficulty=difficulty, attempts=attempts)


def wordle():
    print('\nWelcome to Wordle!')
    attempts = get_input('Enter the number of attempts', Wordle.DEFAULT_ATTEMPTS)

    game = Wordle()
    game.play(attempts=attempts)


def main():
    game_handlers = [guess_the_number, rock_paper_scissors, word_scramble, hangman, wordle]
    print('Welcome to PyGameBox!')

    while True:
        print('\nSelect a game:')
        print('1. Guess the Number')
        print('2. Rock Paper Scissors')
        print('3. Word Scramble')
        print('4. Hangman')
        print('5. Wordle')

        choice = int(input('Enter a number: '))
        if 1 <= choice <= 5:
            game = game_handlers[choice - 1]
            game()
        else:
            print('Invalid input.')


if __name__ == '__main__':
    main()
