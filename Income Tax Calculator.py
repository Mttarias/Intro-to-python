TAX_RATE = float(0.2)
S_DEDUCTION = 10000
dependentDeduction = 0

grossIncome = float(input("Enter the gross income: "))

dependents = int(input("Enter the number of dependents: "))

if dependents > 0:
    dependentDeduction = 3000 * dependents

grossIncome -= S_DEDUCTION + dependentDeduction

incomeTax = TAX_RATE * grossIncome

print("The income tax is $", incomeTax)
