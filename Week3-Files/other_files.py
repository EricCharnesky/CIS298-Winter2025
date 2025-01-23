import csv
import json

class Staff:

    def __init__(self, name):
        self.name = name

staff_list = []

eric = Staff("Eric")

staff_list.append(eric)

with open('staff.json', 'w') as file:
    json.dump(staff_list, file, indent=4)

print(eric)


# https://www.bing.com/search?pglt=297&q=python+json+format&cvid=bc0f14127f31470ab407243e6907cb83&gs_lcrp=EgRlZGdlKgYIABBFGDkyBggAEEUYOTIGCAEQABhAMgYIAhAAGEAyBggDEAAYQDIGCAQQABhAMgYIBRAAGEAyBggGEAAYQDIGCAcQABhAMgYICBAAGEDSAQgxNjA1ajBqMagCALACAA&FORM=ANNTA1&PC=W099
# bing ai answer


data = {
    "name": "Alice",
    "age": 30,
    "city": "Wonderland"
}

# don't overwrite again
#with open('data.json', 'w') as file:
#    json.dump(data, file, indent=4)

# reads the file
with open('data.json', 'r') as file:
    data = json.load(file)

print(data)






data = []

# https://stackoverflow.com/questions/50228008/strange-character-while-reading-a-csv-file
# gets rid of weird ï»¿0 starting character - yay UTF
with open('staff.csv', encoding='utf-8-sig') as staffcsv:
    staff_reader = csv.reader(staffcsv)
    for row in staff_reader:
        print(row)


with open('stocks.csv') as stockscsv:
    reader = csv.reader(stockscsv)
    for row in reader:
        data.append(row)

with open('stocks.json', 'w') as file:
    json.dump(data, file, indent=4)

with open('stocks.json', 'r') as file:
    stock_data = json.load(file)

for row in stock_data:
    print(row)

year_to_lookup = input("Enter the year to start from")
money_invested = float(input("How much money did you invest that year?"))

initial_value = 0

for row in data:
    # terrible way to look this up - N
    if row[0] == year_to_lookup:
        print(row)
        initial_value = float(row[1])

        # -1 is a shortcut for len(whatever) - 1
current_year_row = data[-1]
current_value = float(current_year_row[1])

current_value_money_invested = money_invested * ( current_value / initial_value )

print(f'after {2025-int(year_to_lookup)} years, your {money_invested}'
      f' is now worth ${current_value_money_invested}')





