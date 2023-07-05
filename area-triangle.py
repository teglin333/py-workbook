def computeArea(inputs):
    base, height = inputs
    return (base * height) / 2

def getUserInput():
    base = float(input('Enter the length of the base: '))
    height = float(input('Enter the height: '))
    return [base, height]

print('The area of the triangle is %.2f.' % computeArea(getUserInput()))