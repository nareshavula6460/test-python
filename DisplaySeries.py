n = int(input("Enter the number:"))
sum = 0
lst = []
count = 1;

for i in range(1,n+1):
    if i % 2 != 0:
      sum = sum + i
      count = count + 1
      lst.append(i)
print(sum)
print(lst)










