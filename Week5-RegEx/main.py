import re

with open('poem.txt') as file:
    for line in file.readlines():
        if re.search('I.m', line):
            print(line, end='')
        if "I" in line and line[line.find("I") + 2] == 'm':
            print(line, end='')



# umgpt: prompt
# write a regex that looks for dates in the format mm/dd/yyyy in a string
# can you make it so you can have a 1 digit month or day>
# please escape the forward slashes
# can it also check for the european format mm/dd/yyyy and the iso format yyyy-mm-dd
# make it so they can use forward slashes or dashes for seperators
# validating a date

with open('poem.txt') as file:
    for line in file.readlines():
        for date in re.findall(r'\b(0?[1-9]|1[0-2])[-\/](0?[1-9]|[12][0-9]|3[01])[-\/]\d{4}\b|\b(0?[1-9]|[12][0-9]|3[01])[-\/](0?[1-9]|1[0-2])[-\/]\d{4}\b|\b\d{4}[-\/](0[1-9]|1[0-2])[-\/](0[1-9]|[12][0-9]|3[01])\b', line):
            print(date)

