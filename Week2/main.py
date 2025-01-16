import math
import random
import matplotlib.pyplot as plt
from fontTools.subset import usage

print(f'Eric Charnesky has {len('Eric Charensky')} letters')

# for formatting output :format specifier
print(f"sqrt of 2 is {2**.5:.3f}")
print(f"sqrt of 2 is {math.sqrt(2)}")

# inclusive of both end  points
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))

def some_function():
    print("Happy Thursday!")

    # order doesn't matter here?
    some_other_function()

def some_other_function():
    print("Go back to bed")

# : suggests a type
def double_this(something_to_double : int):
    print(something_to_double * 2)
    return None # implicit in functions with no return

def multiply_these(first : float, second : float):
    print(first * second)

def print_citation(author : str, publisher : str = "", year : int = ""):
    print(f"Some citation {author}, {publisher} ({year})")


def print_face(character : str):
    print(f'{character}   {character}')
    print(f'  {character}')
    print('')
    print(character*5)

def print_body():
    print('  |')
    print(' \\|/')
    print('  |')
    print('  /\\')


def print_character(letter : str, head_function, body_function):
    head_function(letter)
    body_function()

#
#print_face('x')
#print_body()

# no () when passing functions, just the name
print_character('*', print_face, print_body)


# 10() # gives same TypeError: 'int' object is not callable
# as passing 10 to print_character

print_citation("Eric")
# named arguments - doesn't require positional order
print_citation( year=2025, author='Eric')

some_function()

double_this(10)
double_this("Eric")

multiply_these(4, 2)



def quadratic_intercepts(a : float, b : float, c : float ):
    # check for a isn't 0
    if b**2 - 4 * a * c < 0:
        raise ValueError("No intercepts")
    # ( -b +- sqrt ( b**2 - 4 * a * c) ) / 2*a
    first =  ( -b + math.sqrt(b**2 - 4 * a * c) ) / ( 2 * a )
    second = ( -b - math.sqrt(b**2 - 4 * a * c) ) / ( 2 * a )
    return first, second # packs variables into single object

# auto unpack
first, second = quadratic_intercepts(2, -5, 2)
print(f'Intercepts of 2x^2 -5x + 2 are: {first}, {second}')


# while loops are the same


# for loops are different - always like the enhanced for loop
# pretend it's a vector
numbers = [1, 2, 3, 4, 5]

#for ( int number : numbers ){
#
#}
print(numbers)
# 1 iteration per item in the numbers collection
# essentially read only copies
for number in numbers:
    number = number * 2
    print(number)
print(numbers)

# range gives back a tuple 0 -> not including the number
# range( start, end, step )
# range( start, end )
# range( end )
for i in range(10, 0, -1):
    print(i)


name = 'Eric Charnesky'

for letter in name:
    if letter != ' ':
        print(chr(ord(letter) + 1))
    else:
        print(letter)

play_again = 'y'

while play_again == 'y':

    # validate input in a list
    throw = input("Rock, Paper, or Scissors: ").lower()
    while throw not in ['rock', 'paper', 'scissors']:
        throw = input("Rock, Paper, or Scissors: ").lower()

    computer_throw = random.randint(1, 3)

    if computer_throw == 1:
        computer_throw = 'rock'
    elif computer_throw == 2:
        computer_throw = 'paper'
    else:
        computer_throw = 'scissors'

    if throw == computer_throw:
        print("Draw!")
    elif ( throw == 'rock' and computer_throw == 'scissors' ) or \
            ( throw == 'paper' and computer_throw == 'rock' ) or \
            ( throw == 'scissors' and computer_throw == 'paper' ):
        print("Win!")
    else:
        print("Lose!")


    play_again = input("Do you want to play again? y/n")

# [ index ] of a collection type
print(name[4])

# slicing is a substring, start : end ( not inclusive )
# start and end are option
print(name[0:4])
print(name[:-9])

# strings are immuatble, can't change
name[2] = 'I'