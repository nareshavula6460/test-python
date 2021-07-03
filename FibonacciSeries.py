num = int(input("Enter the number:"))
num1 = 0
num2 = 1
print(num1)
print(num2)

for i in range(2,num):

    sum = num1 + num2
    num1 = num2
    num2 = sum
    print(sum)








