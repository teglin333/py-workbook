# Compute the refund for bottle deposits based on the drink containers
# quantity and size.

big_size = 1.0
big_refund = 0.25
small_refund = 0.10

qty_small = int(input('How many small drink containers, of less than %.1f' 
                  % big_size + ' liters, are you depositing today? '))
qty_large = int(input('How many large drink containers, greater than %.1f' 
                  % big_size + ' liters, are you depositing today? '))

refund = (big_refund * qty_large) + (small_refund * qty_small)

print('Your total refund is: $%.2f. Thank you.' %  refund)

