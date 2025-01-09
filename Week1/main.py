number = 42
print(number)
print(type(number))

some_number_with_decimal = 7.7
print(some_number_with_decimal)
print(type(some_number_with_decimal))

name = 'Eric'
print(name)
print(type(name))

number = name
print(number)
print(type(number))

first_name = 'Eric'
last_name = "Charnesky"

name = first_name + ' ' + last_name
print(name)

print(first_name, last_name, some_number_with_decimal)

print(f"First name: {first_name} last name: {last_name}")

print(first_name, end=" ")
print(last_name, end=' ')
print(some_number_with_decimal)

favorite_food = input("What's your favorite food?")
print(favorite_food, "is great!")

# convert to int
favorite_number = int(input("What's your favorite number?"))
print("your favorite number + 10 is: ", favorite_number + 10)

word = 'nan'
print(word*5, 'batman!' )

print(f'your favorite + 10 is : {favorite_number + 10}!')

if favorite_number < 10:
    print("your favorite number is small")
    favorite_number += 10
    favorite_number = 22
elif favorite_number < 100:
    print("Your favorite number has 2 digits!")
else:
    print("You have a big favorite number!")


temp = int(input("What is the temp outside?"))
weather = input("What is the weather outside?")

if weather == 'snow' and temp < 32:
    print("Bring your snowpants")
elif weather == 'sunny' and temp < 32:
    print("wear pants")
elif weather == 'hot' or temp > 32:
    print("this is a weird winter")
else:
    print("I dunno")

if weather == 'snow':
    if temp < 32:
        print("Snowpants")
    else:
        print("The will melt soon")

initial = input("Enter your first initial")

print(f'unicode value of your initial: {ord(initial[0])}')
print(f'your initial + 1: {chr(ord(initial[0]) + 1)}')

is_true = True

print(type(is_true))


if favorite_number:
    print("Your favorite number isn't 0")
else:
    print("That's a weird favorite number")

name = ""

if name:
    print("Nice name")
else:
    print("Forgot to ask for the name")