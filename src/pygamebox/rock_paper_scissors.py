import random

class RockPaperScissors:

    def __init__(self):
        self.playable = ["Rock", "Paper", "Scissors"]
        self.results = {1: "Player Wins.", -1: "Computer Wins.", 0: "Draw."}

    def get_user_throw(self):
        print("Choose your throw:")
        for i, label in enumerate(self.playable, start=1):
            print(f'{i}. {label}')
        while True:
            user_input = input("> ")
            if self.validate_input(user_input):
                return int(user_input) - 1

    def validate_input(self, user_input):

        if (isinstance(user_input, int)):
            if 1 <= user_input <= 3:
                return True
            return False
        
        if user_input.isdigit():
                user_input = int(user_input)
                if 1 <= user_input <= 3:
                    return True        
        print("Please enter a valid choice.")
        return False

    def throw(self):
        return random.randint(0, 2)

    def round(self, user_throw, computer_throw):
        if user_throw == (computer_throw + 1) % 3:
            result = 1
        elif computer_throw == (user_throw + 1) % 3:
            result = -1
        else:
            result = 0
        return result
    
    def validate_round_input(self, round_input):

        if (isinstance(round_input, int)):
            if (round_input >= 1):
                return True
            
        return False

    def play(self, rounds = 1):

        if self.validate_round_input(rounds):
            for i in range(rounds):
                while True:
                    user_throw = self.get_user_throw()
                    computer_throw = self.throw()
                    print(f"You threw {self.playable[user_throw]}")
                    print(f"Computer threw {self.playable[computer_throw]}")
                    result = self.round(user_throw, computer_throw)
                    print(self.results[result])
                    if result != 0:
                        break
        else:
            print("Please enter a valid number of rounds to play.")

