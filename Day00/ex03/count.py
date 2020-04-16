import string
import sys


def count(text):
    upper = 0
    space = 0
    lower = 0
    punc = 0
    for x in text:
        if x.isupper():
            upper += 1
        elif x.islower():
            lower += 1
        elif x == " ":
            space += 1
        elif x in string.punctuation:
            punc += 1
    print(
        f"The text contains {len(text)} characters:\n\
- {upper} upper letters\n\n\
- {lower} lower letters\n\n\
- {punc} punctuation marks\n\n\
- {space} spaces"
    )


def text_analyzer(text=None):
    """This function counts the number of upper characters, lower characters, 
    punctuation and spaces in a given text.
    """
    while text == None or len(text) == 0:
        text = input("What is the text to analyse?\n")
    count(text)


if __name__ == "__main__":
    text_analyzer()
