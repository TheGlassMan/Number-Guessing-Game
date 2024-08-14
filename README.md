# Number-Guessing-Game
It would be easy to make a simple Python Gussing Game in the terminal using basic code like the one below
` randNum = random.randint(1,100)
    tries = 0
    winnerCheck = False
    print("Welcome to Guess The Number Please enter a number (1-100)")
    guessNum = int(input())
    while(winnerCheck == False):
        tries+=1
        if (guessNum >= 1 and guessNum <= 100):
            if (guessNum == randNum):
                print(f"Congrats you won in {tries} tries!!")
                winnerCheck = True
            elif (guessNum > randNum):
                print(f"{guessNum} is too high please try again")
                guessNum = int(input())
            else:
                print(f"{guessNum} is too low please try again")
                guessNum = int(input())
        else:
            print("Number invalid please enter another number")
            guessNum = int(input())`
However using the knowlege I learned from my Media Downloader Project I was able to learn more about tkinter and customtkinter to create a GUI for the game to be able to play it in a more comfortable environment
