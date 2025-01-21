
class_name = input("Enter the name of your class")
number_of_assignments = 0

try:
    gradebook = open(f'{class_name}.txt')
    names = []
    scores = []
    name = gradebook.readline()
    while name:
        number_of_assignments = int(gradebook.readline())
        assignment_scores = []
        for assignment in range(number_of_assignments):
            score = float(gradebook.readline())
            assignment_scores.append(score)
        names.append(name.strip())
        scores.append(assignment_scores)
        number_of_assignments = len(assignment_scores)
        name = gradebook.readline()


except:
    gradebook = open(f'{class_name}.txt', 'w')
    gradebook.close()
    names = []
    scores = []


choice = ""

while choice != "5":
    print("1 - add student")
    print("2 - edit student")
    print('3 - display entire gradebook')
    print('4 - add assignment')
    print('5 - save and quit')
    choice = input()

    if choice == '1':
        name = input("Enter the student name")
        assignment_scores = []
        for assignment in range(number_of_assignments):
            score = float(input(f"Enter the score for assignment #{assignment}"))
            assignment_scores.append(score)
        names.append(name)
        scores.append(assignment_scores)

    elif choice == '2':
        name = input("Enter the student to edit")
        try:
            index = names.index(name)
            print(f"current score {scores[index]}")
            assignment_scores = []
            for assignment in range(number_of_assignments):
                score = float(input(f"Enter the score for assignment #{number_of_assignments}"))
                assignment_scores.append(score)

            scores[index] = assignment_scores
        except:
            print("student not found, please try again")

    elif choice == '3':
        for index in range(len(names)):
            print(f'{names[index]} - {scores[index]}')
        #print(f'average score: {sum(scores)/len(scores)}')

    elif choice == '4':
        number_of_assignments += 1
        for index in range(len(names)):
            score = float(input(f"enter the score for the assignment for {names[index]}"))
            scores[index].append(score)

    elif choice == '5':
        # auto close when we're done
        with open(f'{class_name}.txt', 'w') as gradebook:
            for index in range(len(names)):
                gradebook.write(f'{names[index]}\n')
                gradebook.write(f'{len(scores[index])}\n')
                for score in scores[index]:
                    gradebook.write(f'{score}\n')