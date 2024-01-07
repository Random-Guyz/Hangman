from tkinter import*
from tkinter import messagebox
from string import ascii_uppercase
import random

win = Tk()
win.title('Hangman-Guess Friend Name')
win.minsize(600, 400)
win.configure(bg='lightblue')  # Set the background color to light blue

friends = ['NITESH', 'KAIF', 'YOGESH', 'MOIN', 'SARTHAK', 'SANKET', 'ASHISH', 'VINNEET', 'SADIK', 'GAURAV', 'UMAIR',
        'LALIT', 'MANAS', 'SUMIT', 'SANDESH', 'KETAN', 'KUNAL' , 'Haider']

photos = [PhotoImage(file="images/hang0.png"), PhotoImage(file="images/hang1.png"), PhotoImage(file="images/hang2.png"),
        PhotoImage(file="images/hang3.png"), PhotoImage(file="images/hang4.png"), PhotoImage(file="images/hang5.png"),
        PhotoImage(file="images/hang6.png"), PhotoImage(file="images/hang7.png"), PhotoImage(file="images/hang8.png"),
        PhotoImage(file="images/hang9.png"), PhotoImage(file="images/hang10.png"), PhotoImage(file="images/hang11.png")]

def new_game():
    global word_with_spaces
    global num_of_guesses
    num_of_guesses = 0

    word = random.choice(friends)
    word_with_spaces = " ".join(word)
    lbl_word.set(' '.join("_" * len(word)))

def guess_letter(letter):
    global num_of_guesses
    if num_of_guesses < 11:
        txt = list(word_with_spaces)
        guessed = list(lbl_word.get())
        if word_with_spaces.count(letter) > 0:
            for c in range(len(txt)):
                if txt[c] == letter:
                    guessed[c] = letter
            lbl_word.set("".join(guessed))
            if lbl_word.get() == word_with_spaces:
                messagebox.showinfo("Hangman", "You guessed it!")
        else:
            num_of_guesses += 1
            img_lbl.config(image=photos[num_of_guesses])
            if num_of_guesses == 11:
                messagebox.showwarning("Hangman", "Game Over")

img_lbl = Label(win)
img_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=40)

lbl_word = StringVar()
Label(win, textvariable=lbl_word, font=('consolas 24 bold'), bg='lightblue').grid(row=0, column=3, columnspan=6, padx=10)

n = 0
for c in ascii_uppercase:
    Button(win, text=c, command=lambda c=c: guess_letter(c), font=('Helvetica 18'), width=4, bg='lightblue').grid(row=1 + n // 9, column=n % 9)
    n += 1

Button(win, text="New\nGame", command=lambda: new_game(), font=("Helvetica 10 bold"), bg='lightblue').grid(row=3, column=8)

new_game()
win.mainloop()
