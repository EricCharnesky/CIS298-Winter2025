
def get_total(prompt):
    total = 0
    value = -1
    while value != 0:
        value = float(input(f'{prompt} or 0 to stop'))
        total += value
    return total


BRACKET_START_VALUES_AND_RATE = { 0 : .1
    , 11_600: .12, 47_150: .22, 100_525 : .24
    , 191_950 : .32, 243_725 : .35, 609_350 : .37 }
STANDARD_DEDUCTION = 14_600


gross_income = get_total("Enter an income")
total_deductions = get_total("Enter a deduction")

if total_deductions < STANDARD_DEDUCTION:
    total_deductions = STANDARD_DEDUCTION

adjusted_gross_income = gross_income - total_deductions
income_to_be_taxed = adjusted_gross_income

tax_rates_and_taxes_owed = {}

bracket_starts = list(BRACKET_START_VALUES_AND_RATE.keys())
bracket_starts.sort(reverse=True)

for bracket_start in bracket_starts:
    tax_rates_and_taxes_owed[BRACKET_START_VALUES_AND_RATE[bracket_start]] = 0
    if income_to_be_taxed > bracket_start:
        tax_rates_and_taxes_owed[BRACKET_START_VALUES_AND_RATE[bracket_start]] = \
            (income_to_be_taxed - bracket_start) * BRACKET_START_VALUES_AND_RATE[bracket_start]
        income_to_be_taxed = bracket_start


tax_rates = list(tax_rates_and_taxes_owed.keys())
tax_rates.sort()

for tax_rate in tax_rates:
    print(f'Taxes owed at {tax_rate*100}%: ${tax_rates_and_taxes_owed[tax_rate]:,}')

total_taxes = sum(tax_rates_and_taxes_owed.values())
print(f'Total Taxes Owed: ${total_taxes:,}')
print(f'Taxes as % of Gross Income {total_taxes/gross_income*100:.2f}%')
print(f'Taxes as % of Adjusted Gross Income {total_taxes/adjusted_gross_income*100:.2f}%')



