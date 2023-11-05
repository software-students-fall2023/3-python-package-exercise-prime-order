from colorama import Fore, Back, Style
import random
from pathlib import Path
class Wordle:
    def __init__(self):
        self.guesses = 0
        self.path = Path(__file__).parent.absolute() / "data"
        self.word = self.get_word(self.path / 'words.txt')
        self.words = []

    def get_word(self, path):
        with open(path, 'r') as f:
            words = f.readlines()
        words = [word.strip().lower() for word in words]

        return random.choice(words)
    
    def get_user_input(self):
        return input('Guess a word:')

    def validate_input(self, guess):
        if len(guess) != len(self.word):
                print('Please enter a word of the correct length')
                return False
        return True
            
    def play(self):
        print( self.word )
        while self.guesses < 5:
            print(f'You have {5 - self.guesses} guesses left')
            user_word = self.get_user_input()
            if self.validate_input(user_word):
                if self.check_win(user_word):
                    print('CONGRATULATIONS! YOU WIN!')
                    self.words.append(self.word)
                    self.print_output(user_word)
                    return
                else:
                    self.words.append(user_word)
                    self.print_output(user_word)
                    self.guesses += 1

    def check_win(self, predict):
        if predict == self.word:
            return True
        return False

    def print_output(self, predict):
        for i in range(len(self.words)):
            for j  in range(len(self.words[i])):
                if self.words[i][j] == self.word[j]:
                    print(Fore.GREEN + self.words[i][j], end='  ')
                    print(Style.RESET_ALL, end='')
                elif self.words[i][j] in self.word:
                    print(Fore.YELLOW + self.words[i][j], end='  ')
                    print(Style.RESET_ALL, end='')
                else:
                    print(self.words[i][j], end='  ')
            print()
            print('--------------')
        