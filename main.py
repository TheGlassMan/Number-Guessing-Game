import random
import time
import tkinter
import customtkinter

# Game Inputs
def Game():
    global randNum, winnerCheck, tries
    guessNum = guess_var.get()
    tries+=1
    if guessNum < 1 or guessNum > 100:
        result_label.configure(text="Number invalid! Enter a number between 1 and 100.")
    else:
        previous_guesses.insert(tkinter.END, guessNum)  # Add the guess to the Listbox
    if guessNum == randNum:
        result_label.configure(text=f"Congrats, you won in {tries} tries!!")
        winnerCheck = True
        Submit.configure(state=tkinter.DISABLED)
        guess.configure(state=tkinter.DISABLED)
    elif guessNum > randNum:
        result_label.configure(text=f"⬇️")
    else:
        result_label.configure(text=f"⬆️")
    tries_label.configure(text=f"Tries: {tries}")

#Config Variables for the start of Game
def StartGame():
    global randNum, winnerCheck, tries
    randNum = random.randint(1,100)
    tries = 0
    winnerCheck = False
    result_label.configure(text="Guess a number between 1 and 100.")
    tries_label.configure(text="Tries: 0")
    Submit.configure(state=tkinter.NORMAL)
    guess.configure(state=tkinter.NORMAL)
    previous_guesses.delete(0, tkinter.END)

# System 
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Number Guess Game")

# UI Elements
title = customtkinter.CTkLabel(app, text="Number Guesser")
title.pack(padx=10,pady=10)

# Number Input
guess_var = tkinter.IntVar()
guess = customtkinter.CTkEntry(app, width=350, height=40, textvariable=guess_var)
guess.pack(pady=10)

# Submit Guess Button
Submit = customtkinter.CTkButton(app, text="Submit Guess", command=Game)
Submit.pack(pady=10)

# Result Label
result_label = customtkinter.CTkLabel(app, text="")
result_label.pack(pady=10)

# Listbox for Previous Guesses
previous_guesses = tkinter.Listbox(app, width=50, height=10)
previous_guesses.pack(pady=10)

# Tries Counter Label
tries_label = customtkinter.CTkLabel(app, text="Tries: 0")
tries_label.pack(pady=10)

# Init Variables
StartGame()

# Run app
app.mainloop()
