# compute the parity bit for groups of 8 bits of even parity

def getParity(sequence):
    if sequence.count("1") % 2 == 0:
        return 0
    else:
        return 1

while True:
    try:
        line = input("Enter 8 bits: 0b")
        if line.count("0") + line.count("1") != 8 or len(line) != 8:
            raise ValueError
        else:
            print("The parity bit should be %d." % getParity(line))
            break
    except:
        print("Invalid input.")
