# calculator

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multi(a, b):
    return a * b


def div(a, b):
    return a / b


def calculations():
    import art
    print(art.logo)
    a = float(input("enter a number"))
    maharshi = True
    while maharshi:
        operations = {
            "+": add,
            "-": sub,
            "*": multi,
            "/": div
        }
        for x in operations:
            print(x)
        operation_sybol = input("enter the operation that you want perform")
        b = float(input("enter a number"))
        calculation = operations[operation_sybol]
        result = calculation(a, b)
        print(f"{a}{operation_sybol}{b}={result}")
        if input('type "y" to continue "n"for result') == "y":
            a = result
        else:
            maharshi = False
            calculations()


calculations()
