'''
     *
    ***
   *****
  *******
 *********

วิธีที่ 1

for x in range(5):
    Star = ""
    for y in range(x+1):
        Star = "*" + ("**"*y)
    print(" " * (5 - x - 1) , Star)

วิธีที่ 2
num = int(input("Enter Number : "))
air = int(num-1)
text = int(2)

for x in range(1):
    print(" " * air , "*")
    for y in range(air):
        print(" " * (air-1) , "*" + "*" * text)
        air -= 1
        text += 2


inputNumber = int(input("Please input : "))             # inputNumber = 5
nullChar = int(inputNumber-1) # =                       # nullChar = 4
text = 2                                                # text = 2

for x in range(1):                                      # x = 0
    print(" " * nullChar , "*")                         # " " * 4 (เคาะคูณ4) , *
    for y in range(nullChar-1):                         # y in 4-1 = 3
        print(" " * (nullChar-1), "*" + "*" * text)     # " " * 4-1 (เคาะคูณ3), * + (*คูณ2)
        nullChar = nullChar - 1
        text = text + 2
'''
num = int(input("number "))
nullText = ""
star = ""
for x in range(num):                # แภว
    nullText = " "*(num -x -1)
    for y in range(x+1): # จำนวน*
        nullText = nullText + "*"
        star = "*" * y
    print(nullText+star)

