import sys


def main():
    if len(sys.argv) <= 1:
        pass
    elif len(sys.argv) == 2 and sys.argv[1].isdigit():
        x = int(sys.argv[1])
        if x == 0:
            print("I'm Zero.")
        elif x % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd")
    else:
        print("ERROR")


if __name__ == "__main__":
    main()
