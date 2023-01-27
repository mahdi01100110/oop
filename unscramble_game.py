import time
import datetime
import os
import random
# Create class that acts as a countdown
def countdown(s):
    """

    Parameters
    ----------
    s :
        

    Returns
    -------

    """
    # Calculate the total number of seconds
    total_seconds = s

    # While loop that checks if total_seconds reaches zero
    # If not zero, decrement total time by one second
    while total_seconds > 0:
        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds=total_seconds)

        # Prints the time left on the timer
        print(timer, end="\r")

        # Delays the program one second
        time.sleep(1)
        
        # Reduces total time by one second
        total_seconds -= 1

    print("Bzzzt! The countdown is at zero seconds!")

def clear_screen():
    """clear the screen by cls command"""
    return os.system('cls')
# Inputs for hours, minutes, seconds on timer

def game():
    ordered_list = []
    unordered_list = []
    user_list = []
    for i in range(5):
            ordered_list.append(random.randint(11,199))
    print("\n welcome to this game << ")
    print("\n memorize the order of number's and <<")
    print("\n you have only 6 sec to memorize <<")
    unordered_list = ordered_list
    print(f"ordered : {ordered_list}")
    countdown(int(6))
    clear_screen()
    unordered_list=random.sample(ordered_list,len(ordered_list)) 
    print(f"unordered : {unordered_list}")
    print("write down element's you saw by order")
    for i in range(len(ordered_list)):
        user_list.append(int(input(f'number {i+1} is --> ').casefold().strip()))
        if ordered_list[i] == user_list[i]:
            print("correct")
        elif ordered_list[i] != user_list[i]:
            print("You lost the game ")
            print(ordered_list)
            break   

    if ordered_list == user_list:
        print("Congratulation ! You won this game :) ")
