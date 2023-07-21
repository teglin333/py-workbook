def caesar_shift(*, string: str, shift: int) -> str:
    """
    Applies the Caesar cipher shift to the input string.
    
    :param str string: 
        The input string to be encrypted.
    :param int shift:
        The number of positions to shift each letter. Positive values shift to
        the right, and negative values shift to the left.
    :return:
        The encrypted string (ciphertext) obtained by applying the Caesar
        cipher shift to the input string.
    :rtype: str      
    """
    result = []
    for char in string:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base ))
        else:
            result.append(char)
    return ''.join(str(char) for char in result)

while True:
    try:
        print(caesar_shift(string=input('Enter a string: '), 
                           shift=int(input('Enter a shift value: '))))
        break
    except:
        print('Invalid input.')