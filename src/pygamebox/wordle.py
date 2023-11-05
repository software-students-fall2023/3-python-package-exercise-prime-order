import random
from .utils import read_file, get_random_word
from colorama import Fore, Style


class Wordle:
    """
    Implementation of a simple Wordle game.
    The player guesses letters to try to figure out the word.
    """

    def __init__(self) -> None:
        self.words = read_file('wordle.txt')
        self.word = ''
        self.guesses = 0

    def reset(self):
        self.word = get_random_word(self.words)
        self.guesses = 0

    @staticmethod
    def get_user_input() -> str:
        return input('> ')

    def validate_input(self, guess):
        if len(guess) != len(self.word):
            print('Please enter a word of the correct length.')
            return False
        return True

    def play(self):
        print(self.word)
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
            for j in range(len(self.words[i])):
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
