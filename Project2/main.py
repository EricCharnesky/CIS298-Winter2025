import csv

BANK_RATE_OF_RETURN = 1.02

with open('BondsAndStocksAnnualReturn.csv') as file:
    csv_reader = csv.reader(file)
    stocks_rate_of_return = []
    bonds_rate_of_return = []

    # skips the first row
    next(csv_reader)
    for row in csv_reader:
        stocks_rate_of_return.append(float(row[1][:-1])/100)
        bonds_rate_of_return.append(float(row[2][:-1])/100)



current_age = int(input("How old are you?"))
retirement_age = int(input("How old do you want to be when you retire?"))

mattress = float(input("How much money do you have saved under your mattress?"))
bank = float(input("How much money do you have saved in the bank?"))
bonds = float(input("How much money do you have saved in bonds?"))
stocks = float(input("How much money do you have invested in stocks?"))

csv_data_to_write = [['age', 'mattress', 'bank', 'bonds', 'stocks', 'total']]

for age in range(current_age, retirement_age):
    print(f"At age {age} you have:")
    print(f"Money under your mattress: ${mattress:,.02f}")
    print(f"Money in the bank: ${bank:,.02f}")
    print(f"Money saved in bonds: ${bonds:,.02f}")
    print(f"Money invested in stocks: ${stocks:,.02f}")
    print(f'Total Retirement Savings: {mattress + bank + bonds + stocks:,.02f}')
    choice = ""
    while choice != "5":
        print("1 - add money under you mattress")
        print("2 - add money to bank savings")
        print("3 - add money to bonds savings")
        print("4 - add money to stocks investment")
        print("5 - all done for this year")
        choice = input()
        if choice != "5":
            money = float(input("How much money are you adding?"))
            if choice == "1":
                mattress += money
            elif choice == "2":
                bank += money
            elif choice == "3":
                bonds += money
            elif choice == "4":
                stocks += money
        else:
            bank *= BANK_RATE_OF_RETURN
            bonds *= (1 + bonds_rate_of_return[age-current_age])
            stocks *= (1 + stocks_rate_of_return[age-current_age])
            csv_data_to_write.append([age, mattress, bank, bonds, stocks, mattress + bank + bonds + stocks])

results_file = open("results.csv", 'w', newline='')
csv_writer = csv.writer(results_file)
csv_writer.writerows(csv_data_to_write)
results_file.close()

total = mattress + bank + bonds + stocks
print("At your desired retirement age")
print(f"Money under your mattress: ${mattress:,.02f}")
print(f"Money in the bank: ${bank:,.02f}")
print(f"Money saved in bonds: ${bonds:,.02f}")
print(f"Money invested in stocks: ${stocks:,.02f}")
print(f'Total Retirement Savings: {total:,.02f}')
print(f'Your purchasing power of your total savings adjusted for inflation {total / 1.02**(retirement_age-current_age)}')

