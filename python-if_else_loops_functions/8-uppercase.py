#!/usr/bin/python3
def uppercase(str):
    for char in str:
        # Check if character is lowercase (ASCII 97-122)
        if ord(char) >= 97 and ord(char) <= 122:
            # Convert to uppercase by subtracting 32
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")
