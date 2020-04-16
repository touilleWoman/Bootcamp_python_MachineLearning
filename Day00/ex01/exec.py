import sys


def main():
    l = []
    if len(sys.argv) > 1:
        s = " ".join(sys.argv[1:])
        s = s[::-1]
        new_s = ""
        for elem in s:
            if elem.isupper():
                elem = elem.lower()
            elif elem.islower():
                elem = elem.upper()
            new_s += elem
        print(new_s)


if __name__ == "__main__":
    main()
