import time

select = input('Select... ')

if select == 'iteration':
    for temp in range(6):
      print("Loop is on iteration number " + str(temp + 1))
    select = input('Select... ')

if select == 'kaboom':
    countdown = 6
    for l in range(6):
        print('You have ' + str(countdown - 1) + ' seconds left!')
        countdown -= 1
        time.sleep(1)
    print('Kaboom!')
    select = input('Select... ')

if select == 'while countdown':
    count = 6
    while count >0:
        count -= 1
        print(count)
        time.sleep(1)
    select = input('Select... ')

if select == 'trip planner':
    def trip_welcome_else():
        destination = input('Choose another destination: ')
        conf = input('Are you sure you want to plan a trip to ' + destination + '''? 
        1: yes
        2: no
        
        Enter here: ''')
        if conf == '1':
            print('''Okay. Let's go!''')
        else:
            trip_welcome_else()

    def trip_welcome():
        print('Welcome to Emile Maps!')
        destination = input('Choose your destination: ')
        conf = input('Are you sure you want to plan a trip to ' + destination + '''? 
        1: yes
        2: no
        
        Enter here: ''')
        if conf == '1':
            print('''Okay. Let's go!''')
        else:
            trip_welcome_else()
    
    trip_welcome()