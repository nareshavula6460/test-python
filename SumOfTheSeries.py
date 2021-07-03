n = int(input("Enter the number:"))
count = 2
res = 1
for i in range(1,n+1):
    res = res + (1/count)
    count += 1
print(res)
