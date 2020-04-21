import sys


def filter():
    if (
        len(sys.argv) != 3
        or sys.argv[1].isdigit() == True
        or sys.argv[2].isdigit() == False
    ):
        print("ERROR")
    else:
        words = sys.argv[1].split()
        nb = int(sys.argv[2])
        print([x for x in words if len(x) > nb])


if __name__ == "__main__":
    filter()
