def add(x,y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def Main():
    print "You choice: \n1:add, 2:subtrct, 3:multiply, 4:divide"
    choice = raw_input(">")

    a = float(raw_input("Your first number:"))
    b = float(raw_input("Your second number:"))

    if choice == '1':
        print a, "+", b, "=", add(a, b)
    elif choice == '2':
        print a, "-", b, "=", subtract(a, b)
    elif choice == '3':
        print a, "X", b, "=", multiply(a, b)
    elif choice == '4':
        print a, "/", b, "=", divide(a, b)
    else:
        print "I don't know what your mean?"


Main()

