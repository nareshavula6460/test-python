num1 = int(input("Enter the number_1:"))
num2 = int(input("Enter the number_2:"))
sub = num1 - num2
if sub < 0:
    sub = -sub
    print(f'the result(difference) is {sub}')
else:
    print(f'the result(difference) is {sub}')
