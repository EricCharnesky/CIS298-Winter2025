number = 0

# the default is open for reading, add 'w' for writing - 'a' for append
# !!!will erase the previous contents
some_file = open("number2.txt", 'a')

while number < 1_000:
    some_file.write(f'{number}\n')
    number += 1

some_file.close()

some_file_to_read = open('test.txt')


line = some_file_to_read.readline()
while line:
    print(line, end="")
    line = some_file_to_read.readline()
print()

some_file_to_read.close()

class_name = input("Enter the name of your class")

try:
    gradebook = open(f'{class_name}.txt')
    names = []
    scores = []
    name = gradebook.readline()
    while name:
        score = float(gradebook.readline())
        names.append(name.strip())
        scores.append(score)
        name = gradebook.readline()


except:
    gradebook = open(f'{class_name}.txt', 'w')
    gradebook.close()
    names = []
    scores = []


choice = ""

while choice != "4":
    print("1 - add student")
    print("2 - edit student")
    print('3 - display entire gradebook')
    print('4 - save and quit')
    choice = input()

    if choice == '1':
        name = input("Enter the student name")
        score = float(input("Enter the students score"))
        names.append(name)
        scores.append(score)

    elif choice == '2':
        name = input("Enter the student to edit")
        try:
            index = names.index(name)
            print(f"current score {scores[index]}")
            new_score = float(input("Enter the new score"))
            scores[index] = new_score
        except:
            print("student not found, please try again")
    elif choice == '3':
        for index in range(len(names)):
            print(f'{names[index]} - {scores[index]}')
        print(f'average score: {sum(scores)/len(scores)}')
    elif choice == '4':
        # auto close when we're done
        with open(f'{class_name}.txt', 'w') as gradebook:
            for index in range(len(names)):
                gradebook.write(f'{names[index]}\n')
                gradebook.write(f'{scores[index]}\n')


#print(number)