inputRound = int(input("Please Enter Number : "))
sum = 0
for x in range(inputRound):
    x = x+1
    inputNumber = int(input("x"+str(x)+":"))
    sum = sum + inputNumber
print(sum)