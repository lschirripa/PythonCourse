expenses = []

num_expenses = int(input("How many expenses do u wanna register?\n"))

for i in range(num_expenses):
    expenses.append(float(input("expense number " + str(i+1) + ': $')))

totalExpensas = sum(expenses)

print("total Expenses: $",totalExpensas, sep='')