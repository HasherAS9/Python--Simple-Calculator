print('CALCULATOR')


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a // b


print("""Choose The Operation
1. +
2. -
3. *
4. /
""")

choice = int(input('OPERATION: '))
a = int(input('NUMBER1: '))
b = int(input('NUMBER2: '))

if choice == 1:
    print(add(a, b))
elif choice == 2:
    print(sub(a, b))
elif choice == 3:
    print(multiply(a, b))
elif choice == 4:
    print(divide(a, b))

print("PROBLEM SOLVED")
