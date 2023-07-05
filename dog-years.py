def calculateDogYears(human_years):
    if human_years >= 2:
        adulthood_years = human_years - 2
        return 21 + adulthood_years * 4
    elif human_years > 0:
        return human_years * 10.5
    else:
        return 0

while True:
    dog_years = calculateDogYears(int(input('Enter your age in years: ')))
    if (dog_years):
        print('That\'s %d dog years.' % dog_years, '%s' % 'You\'re old!' if
              dog_years >= 30 else 'You\'re young!')
        break
    else:
        print('Invalid input.')
        continue