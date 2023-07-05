# compute the tax and tip for a meal

tax_rate = 0.055
tip_rate = 0.18

subtotal = float(input('Enter subtotal: $'))

grand_total = subtotal + (subtotal * tax_rate) + (subtotal * tip_rate)

print('The grand total is $%.2f.' % grand_total)

