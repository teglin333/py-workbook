import random

def randomPassword() -> str:
    """
    Generate a random password, with a length of 7-10 characters randomly
    selected from positions 33 to 126 in the ASCII table.
    """
    length = random.randint(7,10)
    chars = []
    i = 0
    while(i < length):
        chars.append(chr(random.randint(33,126)))
        i += 1
    print(''.join(chars))


def main():
    randomPassword()


if __name__ == "__main__":
    main()