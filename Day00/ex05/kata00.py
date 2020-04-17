def kata():
    tup = (19, 42, 21)
    tup1 = tuple(str(i) for i in tup)
    print(f"The 3 numbers are : {', '.join(tup1)}")

if __name__ == "__main__":
    kata()
    