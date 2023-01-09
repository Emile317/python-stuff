import random
import time

# score
count = 0
correct_count = 0

# mode selection
def intro():
    print('Welcome to The Guessing Game!\n')
    mode = int(input('''
    Select a mode:
    1: Heads or tails
    2: Dice roll
    '''))
    while mode != 1 and mode != 2:
        mode = input("Please type '1' or '2'")
    return mode

chosen_mode = intro()

# core of the game
def coin_flip_guessr(mode=chosen_mode):
    
    # allows variables to be modified inside function
    global count, correct_count
    
    if mode == 1:
        current_game = "Heads or tails"
    elif mode == 2:
        current_game = "Dice roll"
    print("You're playing: " + current_game)
    
    # mode variables
    if mode == 1:
        rnum = random.randint(1,2)
        cd = 'coin'
    elif mode == 2:
        outcome = random.randint(1,6)
        cd = 'dice'
    
    if mode == 1:
        # the coin flip
        if rnum == 1:
            outcome = 'heads'
        else:
            outcome = 'tails'

        # guess taking
        guess = input('Take your guess: ')
        guess = guess.lower()
        while guess != 'heads' and guess != 'tails':
            guess = input("Please type 'heads' or 'tails': ")
    elif mode == 2:
        # guess taking
        guess = input('Take your guess: ')
        string_range = [str(num) for num in range(1,7)]
        while not any(guess == side for side in string_range):
            guess = input("Please type a number between 1 and 6: ")
        guess = int(guess)


    # the happening
    for i in range(3):
        print('.')
        time.sleep(0.5)
    print('The ' + cd + ' landed on ' + str(outcome) + '!')
    if guess == outcome:
        print('You got it right!')
        correct_count += 1
    elif guess != outcome:
        print('WRONG!!!!!!!')
    count += 1
    
    # score counter (including spelling helper)
    t_count = 'times'
    t_correct_count = 'times'
    if count == 1:
        t_count = 'time'
    if correct_count == 1:
        t_correct_count = 'time'
    print("\nYou've guessed", count, t_count, "and got it right", correct_count, t_correct_count, "\n")
    
    loop()


# quit or go again function
def loop():
    global chosen_mode
    
    p = int(input('''
    1: Try again
    2: Quit
    3: Menu
    '''))
    while not p == 1 and not p == 2 and not p == 3:
        p = int(input("Please type '1', '2', or '3'"))

    if p == 1:
        coin_flip_guessr()
    elif p == 2:
        quit()
    elif p == 3:
        coin_flip_guessr(intro())


coin_flip_guessr()