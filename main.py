count=1
turns=1
print("Number of turns is limited to only 9 times!! ")
n=18
while (True):
    guess=int(input("Guess a number :"))
    if (guess<n):
        print("Your guess is too LOW !!!,Increase your value")
        if (turns<=9) :
            left=(9-turns)
            print("Number of turns left:",left)
            turns=turns+1
            count=count+1
            if (left==0):
                print("Your turns are over")
                break
    elif (guess==n):
        print("Great !!!  this is the correct number you guessed")
        if (turns<=9):
            left=(9-turns)
            print("you guessed the correct number in",count,"turns")
            if (left==0):
                print("Your turns are over")
            break
    elif (guess>n):
        print("Your guess is too HIGH !!!,Decrease your value ")
        if (turns<=9):
            left=(9-turns)
            print("Number of turns left:",left)
            turns=turns+1
            count=count+1
            if (left==0):
                print("Your turns are over")
                break