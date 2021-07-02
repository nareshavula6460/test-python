import random
num = random.randint(1,6)
for i in range(1,4):
    gnum = int(input("Enter the guess number in range(1-5):"))
    if(num == gnum):
        print(f'good you guessed number in {i} attempts')
        break
    else:
        print(f'sorry! your guess is wrong and actual number is {num}')
        if i == 3:
            print("you have reached maximum attempts,try again")
