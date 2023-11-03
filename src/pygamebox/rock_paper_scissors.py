import random

class RockPaperScissors:
    playable = ["Rock", "Paper", "Scissors"]

    def get_user_throw(self):
        print("Choose your throw:")
        for i, label in enumerate(self.playable, start=1):
            print(f'{i}. {label}')
        while True:
            user_input = input("> ")
            if user_input.isdigit():
                user_input = int(user_input)
                if 1 <= user_input <= 3:
                    return user_input - 1
            print("Please enter a valid choice.")

    def throw(self):
        return random.randint(0, 2)

    def round(self, user_throw, computer_throw):
        if user_throw == (computer_throw + 1) % 3:
            result = "You Win."
        elif computer_throw == (user_throw + 1) % 3:
            result = "Computer Win."
        else:
            result = "Draw"
        print(result)
        return result

    def play(self):
        while True:
            user_throw = self.get_user_throw()
            computer_throw = self.throw()
            print(f"You threw {self.playable[user_throw]}")
            print(f"Computer threw {self.playable[computer_throw]}")
            result = self.round(user_throw, computer_throw)
            if result != "Draw":
                break
