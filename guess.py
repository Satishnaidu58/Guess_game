print("Please think of a number between 0 and 100!")
low = 0
high = 100
while True:
    guess = (low+high)//2
    print("Is your secret number"+str(guess)+"?")
    userguess=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    
    if userguess=="h":
        high = guess
    elif userguess=="l":
        low= guess
    elif userguess=="c":
        print("Game over. Your secret number was:",guess)
        break
    else:
        print("Sorry, I did not understand your input.")
