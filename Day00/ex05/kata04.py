def kata():
    args = (0, 4, 132.42222, 10000, 12345.67)
    print(f"day_{args[0]:02}, ex_{args[1]:02} : {args[2]:.2f}, {args[3]:.2e}, {args[4]:.2e}")

if __name__ == "__main__":
    kata()
