import random

unchangeable_list = (1, 2, 3, 4, 5)

for value in unchangeable_list:
    print(value)

for index in range(len(unchangeable_list)):
    print(unchangeable_list[index])

# no append option
# unchangeable_list.append()

# no setting items by index
# unchangeable_list[1] = 10



# key value pairs, key : value
grades = { 'Eric' : 'A', 'Jeb' : 'B' }

# add a key and associated value
grades['Journey'] = 'C'

# updates a key with the associated value
grades['Jeb'] = 'A'

for name in grades:
    print(f'{name} : {grades[name]}')

# checks for a given key
if 'Jubilee' in grades:
    print("Jubilee is in the class")
else:
    print("She's not taking the class")

for name, grade in grades.items():
    print(f'{name} : {grade}')

# bad form - should avoid and use an if in check first
try:
    print(f"Jubilee's grade is: {grades['Jubilee']}")
except KeyError as er:
    print(er)

# get can have an option return value, defaults to None
print(f"Jubilee's grade is: {grades.get('Jubilee', 'not in gradebook')}")

number_of_sides = int(input("How many sides are on your die?"))
number_of_rolls = int(input("How many times are you rolling the die?"))




roll_results = { }
for die_value in range(number_of_rolls, number_of_sides*number_of_rolls+1):
    roll_results[die_value] = 0

for roll in range(1000):
    total = 0
    for roll_count in range(number_of_rolls):
        total += random.randint(1, number_of_sides)
    roll_results[total] += 1

print(roll_results)

for roll in roll_results:
    # bing AI : query: python print integer with 2 digits always
    print(f'{roll:02}: {'*'*roll_results[roll]}')


# don't all have to be the same type
from idlelib.colorizer import color_config
from tkinter.ttk import Label

some_colors = [ 'blue', 'red', 'orange', 'green' ] #, 1, 5.4 ]

favorite_color = input("What's your favorite color?")

# found_favorite_color = False
# for color in some_colors:
#     if color == favorite_color:
#         print("We have your color in the list!")
#         found_favorite_color = True
#
# if not found_favorite_color:
#     print("Sorry we don't have your favorite color")

# in operator checks for values in a collection
if favorite_color.lower() in some_colors:
    print("We have your color in the list!")
else:
    print("Sorry we don't have your favorite color")

fancy_colours = [ 'fuchsia', 'lavender', 'magenta' ]

all_colors = some_colors + fancy_colours

print(all_colors)

all_colors.insert(3, 'purple')

print(all_colors)

try:
    # removes first occurrence by value
    all_colors.remove('fucsia')
except ValueError as er:
    print(er)
    # TODO - make this a better message for a user

all_colors.pop()
all_colors.pop(1)

print(all_colors)

# copy of items
for color in all_colors:
    color = color.upper()
    print(color)

print(all_colors)

for index in range(len(all_colors)):
    all_colors[index] = all_colors[index].upper()

print(all_colors)

# slicing - gets a copy
# [ start_index : end_index ( not inclusive ) ]
print(all_colors[1:3])

# default start is index 0 , and default end is len(the_list)
print(all_colors[:])

# negative index assumes
#print(all_colors[2:len(all_colors)-2])
print(all_colors[2:-2])


numbers = [ 1, 2, 3, 4, 6]

print(f'minimum {min(numbers)}')
print(f'maximum {max(numbers)}')
print(f'sum {sum(numbers)}')
print(f'average {sum(numbers)/len(numbers)}')

sentence = input("Enter a sentence")

words = sentence.split()

highest_number_of_occurrences = 0
most_common_word = ''
for word in words:
    if words.count(word) > highest_number_of_occurrences:
        most_common_word = word
        highest_number_of_occurrences = words.count(word)
print(f"the most common word in your sentence is: {most_common_word}")
print(f'It appeared {highest_number_of_occurrences} times')