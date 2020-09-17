lastNumber = int(input("Enter a no. - "))
for row in range(1, lastNumber):
    for column in range(1, row + 1):
        print(column, end=' ')
    print(" ")
