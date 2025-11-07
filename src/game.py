from enum import Enum
from random import choice

class RPSEnum(Enum):
    '''Rock Paper Scissors Enum'''
    rock = 1
    paper = 2
    scissors = 3
    

class RockPaperScissors:
    """Main class for Rock Paper Scissors game.
    """
    
    
    def __init__(self):
        self.choices = [RPSEnum.paper, RPSEnum.rock, RPSEnum.scissors]
        
        

    def get_user_input(self) -> RPSEnum:
        """Get and validate user input.

        Returns:
            RPSEnum: Enum for choices
        """
        corrct_values = ['rock', 'r', 'paper', 'p', 'scissors', 's']
        user_input = ''
        while True:
            user_input = input('Enter your choice ([R]ock, [P]aper, [S]cissors) :').lower()
            if user_input not in corrct_values:
                print('Value is not CORRECT. Please enter correctly!')
                continue
            break
        if user_input == 'rock' or user_input == 'r':
            return RPSEnum.rock
        elif user_input == 'paper' or user_input == 'p':
            return RPSEnum.paper
        else:
            return RPSEnum.scissors
        
    
    def get_computer_choice(self) -> RPSEnum:
        """Use random method to get a choice from computer.

        Returns:
            RPSEnum:
        """
        return choice(self.choices)
    
    
    def judge(self, user_choice:RPSEnum, computer_choice:RPSEnum) -> int:
        """Judge between user and computer choices

        Args:
            user_choice (RPSEnum): input that got from user
            computer_choice (RPSEnum): choice that computer choose randomly

        Returns:
            int:it shows user win or lose : -1 -> loose   0 -> tie   1 -> win
        """
        
        if user_choice is computer_choice:
            return 0
        
        win_combinations = [(RPSEnum.rock, RPSEnum.scissors), (RPSEnum.paper, RPSEnum.rock), (RPSEnum.scissors, RPSEnum.paper)]
        for win_comb in win_combinations:
            if (user_choice is win_comb[0]) and (computer_choice is win_comb[1]):
                return 1
        return -1
            
    
    def play(self):
        """run the game
        - get user choice 
        - get computer choice
        - judge beween them
        - show the result
        """
        user_input = self.get_user_input()
        computer_input = self.get_computer_choice()
        result = self.judge(user_input, computer_input)
        
        messages = ['Tie :|', 'You Won :)', 'You lost :(']    
        print('-------')
        print(messages[result])
        print('-------')
        print(f'your choice: {user_input.name}')
        print(f'computer choice: {computer_input.name}')    



if __name__ == '__main__':
    game = RockPaperScissors()

    while True:
        game.play()
        
        continue_toplay = input('Play again? ([y]/n) :')
        if continue_toplay == 'n':
            break