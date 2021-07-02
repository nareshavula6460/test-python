amount = float(input("Enter the billing amount:"))
discount = 0
if amount > 6000:
    discount = amount * 0.1
net_amount = amount - discount
print(f'billing amount is:{amount}\ndiscount is:{discount}\nnet amount is:{net_amount}')