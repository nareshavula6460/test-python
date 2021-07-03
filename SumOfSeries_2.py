n = int(input("Enter the number:"))
flag = 1
count = 2
for i in range(1,n+1):
    res = flag/(count*count*count)
    count += 1
print(res)