rows = int(input("Enter a value: "))

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print("*" * i)