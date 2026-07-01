x = float(input("Enter the value of the item: "))
y = float(input("Enter the amount you paid: "))
def due_amount(x, y):
    i = y-x
    return i
print(due_amount(x, y))