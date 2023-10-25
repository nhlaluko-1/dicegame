import random

def random_num_generator(): 
    '''function to generate random number for computer and user '''
    return random.randint(1,6)

def user_name():
    '''prompt the user to enter their name
    validate if the user entered alphabets only'''
    user_input = input("Enter your name : ")
    
    while not validation(user_input):
        user_input = input("Enter your name : ")
    return user_input

def validation(username):
    isValid  = True
    if len(username) < 3 or len(username) > 10:
        isValid = False
    
    elif not username.isalpha():
        isValid = False
    
    return isValid
     

def keep_score(user_number,computer_number, user_score, computer_score):
    '''compare the user number to the computer number 
    then update the score and return the score for each'''
    if user_number > computer_number:
        user_score += 1
    elif user_number < computer_number:
        computer_score += 1
    else:
        user_score += 1
        computer_score += 1
        
    
    return computer_score,user_score
    
def playgame(username):
    '''call other functions in the sequence they should run'''
    computer_score = 0
    user_score = 0
    turns = 0
    while turns < 3:
        user_number = random_num_generator()
        computer_number = random_num_generator()
        
        computer_score, user_score = keep_score(
            user_number,
            computer_number, 
            user_score, 
            computer_score
        )
        print(f'{username} : {user_score}')
        print(f'Computer : {computer_score}')
        turns +=1
    
    if computer_score > user_score:
        print("Computer is the Winner!")
    
    elif user_score > computer_score:
        print(f"{username} is the Winner!")
    
    else:
        print("Draw")
    
    
    
def main_function():
    username = user_name()
    playgame(username)
    

if __name__ == "__main__":
    main_function()