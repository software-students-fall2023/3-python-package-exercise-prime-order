import requests

class Hangman:
    def __init__(self, length):
        self.length = length
        self.word = self.get_word(length)
        self.guesses = 0
        self.reset(length)

    def reset(self, length):
        self.word = self.get_word(length)
        self.guesses = 0

    def get_word(self, length):
        #returns words from a 
        word = requests.get(f"https://random-word-api.herokuapp.com/word?length={length}").json()[0]
        return word
    
    def get_user_guess(self):
        return input('Guess a letter: ')
    
    def validate_input(self, guess):
        if len(guess) != 1:
            print('Please enter a single letter')
            return False
        return True
    
    def check_win(self, predict):
        for letter in predict:
            if letter == '_':
                return False
        return True
        
    def play(self):
        print(f"---Guess the {self.length} letter word!---")
        predict = ['_' for i in range(len(self.word))]
        while self.guesses < 5:
            print(f'You have {5 - self.guesses} guesses left')
            print()
            print( predict )
            guess = self.get_user_guess()
            if self.validate_input(guess):
                if guess in self.word:
                    indices = [i for i in range(len(self.word)) if self.word[i] == guess]
                    for i in indices:
                        predict[i] = guess
                    if self.check_win(predict):
                        print('You win!')
                        return True
                else:
                    print('Incorrect!')
                    self.guesses += 1
        print('You lose!')
        return False

