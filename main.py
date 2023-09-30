def binary_add(a, b):
    result = bin(int(a, 2) + int(b, 2))
    return result[2:]

def binary_sub(a, b):
    result = bin(int(a, 2) - int(b, 2))
    return result[2:]

def binary_mul(a, b):
    result = bin(int(a, 2) * int(b, 2))
    return result[2:]

def binary_div(a, b):
    result = bin(int(a, 2) // int(b, 2))
    return result[2:]

while True:
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting...")
        break

    binary_num1 = input("Enter first binary number: ")
    binary_num2 = input("Enter second binary number: ")

    if choice == '1':
        print("Result:", binary_add(binary_num1, binary_num2))
    elif choice == '2':
        print("Result:", binary_sub(binary_num1, binary_num2))
    elif choice == '3':
        print("Result:", binary_mul(binary_num1, binary_num2))
    elif choice == '4':
        if binary_num2 == '0':
            print("Cannot divide by zero!")
        else:
            print("Result:", binary_div(binary_num1, binary_num2))
    else:
        print("Invalid choice!")
