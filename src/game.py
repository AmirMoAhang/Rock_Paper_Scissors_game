from enum import Enum
from random import randint

class RPSEnum(Enum):
    '''Rock Paper Scissors Enum'''
    rock = 1
    paper = 2
    scissors = 3
    

class RockPaperScissors:
    '''To run the game call game method'''
    
    
    def __init__(self):
        pass

    def get_user_input(self):
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
        
    
    def get_computer_choice(self):
        random_int = randint(1,3)
        return RPSEnum(random_int)
    
    
    def judge(self, user_choice, computer_choice):
        if user_choice is RPSEnum.rock:
            if computer_choice is RPSEnum.rock:
                return 0
            elif computer_choice is RPSEnum.paper:
                return -1
            else:
                return 1
        
        elif user_choice is RPSEnum.paper:
            if computer_choice is RPSEnum.paper:
                return 0
            elif computer_choice is RPSEnum.rock:
                return 1
            else:
                return -1
            
        elif user_choice is RPSEnum.scissors:
            if computer_choice is RPSEnum.scissors:
                return 0 
            elif computer_choice is RPSEnum.rock:
                return -1
            else:
                return 1
            
    
    def game(self):
        user_input = self.get_user_input()
        computer_input = self.get_computer_choice()
        result = self.judge(user_input, computer_input)
        
        messages = ['Tie :|', 'You Won :)', 'You lost :(']    
        print(messages[result])
        print('-------')
        print(f'your choice: {user_input.name}')
        print(f'computer choice: {computer_input.name}')    