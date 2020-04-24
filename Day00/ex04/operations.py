import sys


def operations(x, y):
    if x.lstrip("-").isdigit() and y.lstrip("-").isdigit():
        x = int(x)
        y = int(y)
        if y == 0:
            div = "ERROR (div by zero)"
            modulo = "ERROR (modulo by zero)"
        else:
            div = x / y
            modulo = x % y
        print(
            f"sum:         {x + y}\n"
            f"Difference:  {x - y}\n"
            f"Product:     {x * y}\n"
            f"Quotient:    {div}\n"
            f"Remainder:   {modulo}")
    else:
        print(
            "InputError: only numbers\n"
            "Usage: python operations.py\n"
            "Example:\n"
            "   python operations.py 10 3"
        )


def check_arg():
    if len(sys.argv) < 3:
        print(
            "Usage: python operations.py\n" "Example:\n" "   python operations.py 10 3"
        )
    elif len(sys.argv) > 3:
        print(
            "InputError: too many arguments\n"
            "Usage: python operations.py\n"
            "Example:\n"
            "   python operations.py 10 3"
        )
    else:
        operations(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    check_arg()
