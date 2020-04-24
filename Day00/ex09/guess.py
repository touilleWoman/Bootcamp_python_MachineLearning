import random


def guess():
    nb = random.randint(1, 99)
    print(
        "This is an interactive guessing game!\n"
        "You have to enter a number between 1 and 99 to find out the secret number.\n"
        "Type 'exit' to end the game.\n"
        "Good luck!\n"
    )
    count = 0
    while True:
        cmd = input("What's your guess between 1 and 99?\n")
        count += 1
        if cmd == "exit":
            print("Goodbye!")
            break
        if not cmd.isdigit():
            print("That's not a number.")
        elif int(cmd) < nb:
            print("Too low!")
        elif int(cmd) > nb:
            print("Too high!")
        elif int(cmd) == nb:
            if count == 1:
                if nb == 42:
                    print(
                        "The answer to the ultimate question of life, the universe and"
                        "everything is 42."
                    )
                print("Congratulations! You got it on your first try!")
            else:
                print(
                    "Congratulations, you've got it!\n" f"You won in {count} attempts!"
                )
            break


if __name__ == "__main__":
    guess()
