correctNumber = 17
userGuess = 0                   # อย่าลืมประกาศค่าเริ่มต้น
while userGuess != correctNumber:
    userGuess = int(input("Please Guess a number : "))
    if userGuess > correctNumber:
        print("Too Large")
    elif userGuess < correctNumber:
        print("Too Small")
    elif userGuess == correctNumber:
        print("Correct !")


