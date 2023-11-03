import random

class GuessTheNumber:

    def __init__(self, start=1, end=100):
        self.start = start
        self.end = end
        self.reset()

    def reset(self):
        self.number = random.randint(self.start, self.end)
        self.guesses = 0

    def get_user_guess(self):
        return input(f'Guess a number between {self.start} and {self.end}: ')
    
    def validate_input(self, guess):
        try:
            guess = int(guess)
            if guess < self.start or guess > self.end:
                raise ValueError
        except (ValueError, TypeError):
            print('Please enter a valid number within the range')
            return False
        return True

    def guess(self, user_guess):
        if user_guess < self.number:
            return -1
        elif user_guess > self.number:
            return 1
        else:
            return 0
    
    def turn(self, user_guess):
        if self.validate_input(user_guess):
            self.guesses += 1
            user_guess = int(user_guess)
            result = self.guess(user_guess)
            if result == -1:
                print('Too low')
            elif result == 1:
                print('Too high')
            else:
                print(f'You guessed it in {self.guesses} guesses')
                return True
        return False
    
    def play(self):
        while True:
            user_guess = self.get_user_guess()
            if self.turn(user_guess):
                break