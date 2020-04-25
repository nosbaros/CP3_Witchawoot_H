inputNumber = int(input("Please input : "))
'''text = ""
for i in range(inputNumber):
    text = text + "*"
print(text)
'''
# #print(inputNumber * "*")    #สั้นกว่า การคูณกับ string ก็ใช้วิธีนี้ง่ายกว่า
'''
text = ""
for i in range(inputNumber):
    text = text + "*"
    print(text)
'''

for x in range(inputNumber):
    text = ""
    for y in range(x+1):
        text = text + "*"
    print(text)
