import time

print('Welcome to the game! quiz')
intro = input('Do you want to play? ')
if intro != 'yes':
    print('Well bye then fuck you')
    quit()
else:
    print('Yoo lets go then')
    time.sleep(1)

question1 = "Spell the word 'you' "
question2 = "Keyboard and? "
question3 = "Is Python a programming language or an animal? "
answer1 = 'you'
answer2 = 'mouse'
answer3 = 'a programming language'

points = 0

user_answer1 = input(question1)
if user_answer1 == answer1:
    points += 1
    print("That's correct! You earned 1 point, you now have", points, 'points')
    time.sleep(1)
else:
    print("How on earth did you get that shit wrong? Piece of shit dumbass bitchass. The right answer is", answer1)

proceed = input('Do you want to proceed to the next question? ')
if proceed != 'yes':
    print('goodbye')
    quit()
else:
    print("Here comes the next question:")
    time.sleep(1)

user_answer2 = input(question2)
if user_answer2 == answer2:
    points += 1
    print("That's correct! You earned 1 point, you now have", points, 'points')
    time.sleep(1)
else:
    print("I'm really starting to doubt you. The right answer is", answer2)

proceed = input('Do you want to proceed to the next question? ')
if proceed != 'yes':
    print('goodbye')
    quit()
else:
    print("Here comes the next question:")
    time.sleep(1)

user_answer3 = input(question3)
if user_answer3 == answer3:
    points += 1
    print("That's correct! You earned 1 point, you now have", points, 'points')
else:
    print("I guess the questions are getting a little harder. The right answer is", answer3)

if points == 3:
    print("You won the quiz! Congratulations!")
else:
    print("You didn't quite win. Try better next time!")

quit()