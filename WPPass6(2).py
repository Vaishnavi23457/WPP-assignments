import random

class Rock_Paper_Scissors():
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.rounds = 0
        self.choices = ['rock', 'paper', 'scissors']
    
    def play(self):
        while self.rounds < 3:
            self.rounds += 1
            self.player = input('Enter your choice: ').lower()
            self.computer = random.choice(self.choices)
            print(f'Computer chose: {self.computer}')
            if self.player == self.computer:
                print('Tie')
            elif self.player == 'rock':
                if self.computer == 'paper':
                    print('Computer wins')
                    self.computer_score += 1
                else:
                    print('Player wins')
                    self.player_score += 1
            elif self.player == 'paper':
                if self.computer == 'scissors':
                    print('Computer wins')
                    self.computer_score += 1
                else:
                    print('Player wins')
                    self.player_score += 1
            elif self.player == 'scissors':
                if self.computer == 'rock':
                    print('Computer wins')
                    self.computer_score += 1
                else:
                    print('Player wins')
                    self.player_score += 1
            else:
                print('Invalid choice')
        if self.player_score > self.computer_score:
            print('Player wins the game')
        elif self.player_score < self.computer_score:
            print('Computer wins the game')
        else:
            print('Tie')

    def call(self):
        print("Enter number of test cases:")
        n = int(input())
        for i in range(n):
            self.play()

game = Rock_Paper_Scissors()
game.call()
