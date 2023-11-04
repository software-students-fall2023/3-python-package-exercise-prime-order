import random
from pathlib import Path

DATA_DIR = Path(__file__).parent.absolute() / "data"

class WordScramble:

    def __init__(self):

        self.all_words = self.read_word_file(DATA_DIR / 'words.txt')

        self.easy_words = [word for word in self.all_words if len(word) <= 4]
        self.medium_words = [word for word in self.all_words if 5 <= len(word) <= 7]
        self.hard_words = [word for word in self.all_words if len(word) >= 8]

        self.difficulty_word_list = {1: self.easy_words,
                                     2: self.medium_words,
                                     3: self.hard_words}
        
    def read_word_file(self, file_path):

        words = []

        with open(file_path, 'r') as file:
            for line in file:
                words.append(line.strip().lower())
        
        return words

    def get_random_word(self, word_list):
        return random.choice(word_list)
    
    def scramble_word(self, word):

        while True:

            word_chars = list(word)
            random.shuffle(word_chars)
            shuffled_word = ''.join(word_chars)
            if (shuffled_word != word):
                return shuffled_word
    
    def get_word_list(self, difficulty):
        return self.difficulty_word_list[difficulty]
    
    def play(self, difficulty = 1, attempts = 1):

        word_list = self.get_word_list(difficulty)
        word_to_guess = self.get_random_word(word_list)
        scrambled_word = self.scramble_word(word_to_guess)

        print(f"Welcome to Word Scramble Game Level {difficulty} !")
        print("Unscramble the word:", scrambled_word)

        while (attempts):

            user_input = input().lower()
            if (user_input == word_to_guess):
                print(f"You got it! The word was : {word_to_guess}")
                break
            else:
                attempts -= 1
                if (attempts):
                    print(f"Incorrect. You have {attempts} attempts left. Good Luck!")

                else:
                    print(f"Incorrect. You have no attempts left. The word was {word_to_guess}")






