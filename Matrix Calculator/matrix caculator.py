print("**** Welcome to Matrix Calculator ****")

while True:
    list1 = []
    list2 = []
    temp_column = 0
    print("Calculator Functions:")
    print("1. Addition\n2. Substraction")
    command = input("Enter your choice (1/2): ")
    row = int(input("Enter the number of row: "))
    for i in range(row):
        matrix1 = input("Enter the first matrix: ").split()
        for y in matrix1:
            list1.append(int(y))
            temp_column += 1
    for j in range(row):
        matrix2 = input("Enter the second matrix: ").split()
        for z in matrix2:
            list2.append(int(z))
    if command == "1":
        for a in range(len(list1)):
            list1[a] = list1[a]+list2[a]
    elif command == "2":
        for a in range(len(list1)):
            list1[a] = list1[a]-list2[a]
    column = int(len(list1)/row)
    start = 0
    end = column
    result = ""
    for x in range(row):
        for y in range(start, end):
            result += str(list1[y])+" "
        result += "\n"
        start += column
        end += column
    if command == "1":
        print("The Summation of the matrixs:")
    elif command == "2":
        print("The Substraction of the matrixs:")
    print(result)
