# Mainly just playing around with functions from a Codecademy project, but decided to make a number abbreviator!


train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Rounds large numbers and adds abbreviation
def number_letter_maker(number):
  if number >= 1000 and number < 1000000:
    number = round(number / 1000, 2)
    if number - int(number) == 0:
      number_int = int(number)
      number_int = str(number_int) + 'K'
      return number_int
    else:
      number = str(number) + 'K'
      return number
  elif number >= 1000000 and number < 1000000000:
    number = round(number / 1000000, 2)
    if number - int(number) == 0:
      number_int = int(number)
      number_int = str(number_int) + 'M'
      return number_int
    else:
      number = str(number) + 'M'
      return number
  elif number >= 1000000000 and number < 1000000000000:
    number = round(number / 1000000000, 2)
    if number - int(number) == 0:
      number_int = int(number)
      number_int = str(number_int) + 'B'
      return number_int
    else:
      number = str(number) + 'B'
      return number
  elif number >= 1000000000000 and number < 1000000000000000:
    number = round(number / 1000000000000, 2)
    if number - int(number) == 0:
      number_int = int(number)
      number_int = str(number_int) + 't'
      return number_int
    else:
      number = str(number) + 't'
      return number
  elif number >= 1000000000000000 and number < 1000000000000000000:
    number = round(number / 1000000000000000, 2)
    if number - int(number) == 0:
      number_int = int(number)
      number_int = str(number_int) + 'q'
      return number_int
    else:
      number = str(number) + 'q'
      return number
  elif number >= 1000000000000000000 and number < 1000000000000000000000:
    number = round(number / 1000000000000000000, 2)
    if number - int(number) == 0:
      number_int = int(number)
      number_int = str(number_int) + 'Q'
      return number_int
    else:
      number = str(number) + 'Q'
      return number
  elif number >= 1000000000000000000000 and number < 1000000000000000000000000:
    number = round(number / 1000000000000000000000, 2)
    if number - int(number) == 0:
      number_int = int(number)
      number_int = str(number_int) + 's'
      return number_int
    else:
      number = str(number) + 's'
      return number
  else:
    return number

# other functions
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

def get_force(mass, acceleration):
  force = mass * acceleration
  return force

def get_energy(mass, c = 3*10**8):
  energy = mass * c**2
  return energy

def get_work(mass, acceleration, distance):
  work = get_force(mass, acceleration) * distance
  return work

#end of functions

train_force = get_force(train_mass, train_acceleration)
#print('The GE train supplies ' + str(number_letter_maker(train_force)) + ' Newtons of force.')

bomb_energy = get_energy(bomb_mass)
#print('A 1kg bomb supplies ' + str(number_letter_maker(bomb_energy)) + ' Joules')

train_work = get_work(train_mass, train_acceleration, train_distance)
#print('The GE train does ' + str(number_letter_maker(train_work)) + ' Joules of work over ' + str(number_letter_maker(train_distance)) + ' meters.')

print('''Hello, welcome to Emile's number abbreviator!''')
print('''In this program you can put in a number and it will round it to two decimals and putting the abbreviation of the number behind it.
E.g if you put in 19232 the program will output ''' + number_letter_maker(19232) + '.')

def input_num():
    input_num = input('Put in any number: ')
    input_num_int = int(input_num)
    return input_num_int

input_num = input_num()

def answer():
    if input_num < 1000:
        print('Your number is too low! Please put in a higher number below.')
        input_num()
    elif input_num >= 10**24:
        print('Your number is too high! Please put in another number below.')
        input_num()
    else:
        print('Here is your abbreviated number: ' + number_letter_maker(input_num))
        print('''Do you want to abbreviate another number?
        
        Please select an option:
        1: yes
        2: no
        ''')
        second_input_num = input('')

        if second_input_num == '1':
            input_num()
            answer()
        elif second_input_num == '2':
            input_num()
            answer()
        else:
            second_input_num = input('Please select a valid option: ')
            if second_input_num == '1':
                input_num()
                answer()
            elif second_input_num == '2':
                input_num()
                answer()
            else:
                print('fuck off, idk how to make this work how hard is it to put in a number i gave you a second chance even.')
                quit()
                
answer()
