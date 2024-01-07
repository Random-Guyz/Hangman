import tkinter
from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random

global hints

hints = {
    'PYTHON': 'CODE',
    'JAVA': 'CODE',
    'HTML': 'CODE',
    'CSS': 'CODE',
    'JAVASCRIPT': 'CODE',
    'MAHARASHTRA': 'STATE',
    'DELHI': 'STATE',
    'GUJARAT': 'STATE',
    'CRICKET': ' SPORT',
    'FOOTBALL': ' SPORT',
    'KABBADI': ' SPORT',
    'MONITOR': 'HARDWARE',
    'MOUSE': 'HARDWARE',
    'KEYBOARD': 'HARDWARE',
    'CPU': 'HARDWARE',
    'APPLE': ' FRUIT',
    'MANGO': ' FRUIT',
    'BANANA': 'FRUIT'
}


def new_game():
    global word_with_spaces
    global num_of_guesses
    num_of_guesses = 0

    word = random.choice(new_Words)
    random_Hint.set(hints[word])
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


def create_keyboard(win):
    keys = [
        'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
        'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
        'Z', 'X', 'C', 'V', 'B', 'N', 'M'
    ]

    row = 5
    col = 0
    for key in keys:
        button = Button(win, text=key, width=8, command=lambda k=key: guess_letter(
            k), font=('consolas 24 '), bg='#f4ac60')
        button.grid(row=row, column=col, sticky="w")
        win.grid_columnconfigure(col, weight=1)
        col += 1
        if col > 9:  # Change the number of columns based on the layout you want
            col = 0
            row += 1


def initialize_menu_window():
    menu_window = Tk()
    menu_window.title('Hangman-Guess Friend Name - Menu')
    menu_window.minsize(600, 400)
    menu_window.configure(bg='#f4ac60')
    return menu_window


def create_menu(menu_window, hangman_window):
    hangman_title_text = StringVar()
    hangman_title_text.set("Hangman Game")
    hangman_title = Label(menu_window, textvariable=hangman_title_text, font=(
        'consolas 100 '), bg='#f4ac60')
    logo = PhotoImage(
        file=r"images\hangman.gif")
    hangman_title.grid(row=0, column=5)
    menu_window.grid_columnconfigure(5, weight=1)
    menu_window.grid_rowconfigure(5, weight=1)
    menu_window.grid_rowconfigure(7, weight=1)

    new_game_button = Button(menu_window, text="New Game", command=lambda: start_game(
        menu_window, hangman_window), width=50, font=('consolas 15 bold'), bg='#f4ac60')
    new_game_button.grid(row=5, column=5)

    quit_button = Button(menu_window, text="Quit Game", command=lambda: quit_game(
        menu_window), width=50, font=('consolas 15 bold'), bg="#f4ac60")
    quit_button.grid(row=6, column=5)

    logo_label = Label(menu_window, image=logo, bg="#f4ac60", width=1)
    logo_label.grid(row=0, column=1)


def initialize_hangman_window():
    win = tkinter.Toplevel()
    win.title('Hangman-Guess Friend Name')
    win.minsize(600, 400)
    win.configure(bg='#f4ac60')
    win.withdraw()
    return win


def start_game(menu_window, hangman_window):
    menu_window.withdraw()
    hangman_window.deiconify()


def return_to_main_menu(menu_window, hangman_window):
    hangman_window.withdraw()
    menu_window.deiconify()


def quit_game(menu_window):
    menu_window.quit()


menu_window = initialize_menu_window()
win = initialize_hangman_window()

create_menu(menu_window, win)

new_Words = ['PYTHON', 'JAVA', 'HTML', 'CSS', 'JAVASCRIPT', 'MAHARASHTRA', 'DELHI', 'GUJARAT', 'CRICKET', 'FOOTBALL', 'KABBADI',
             'MONITOR', 'MOUSE', 'KEYBOARD', 'CPU', 'APPLE', 'MANGO', 'BANANA']

photos = [PhotoImage(file="images/hang0.png"), PhotoImage(file="images/hang1.png"), PhotoImage(file="images/hang2.png"),
          PhotoImage(file="images/hang3.png"), PhotoImage(
              file="images/hang4.png"), PhotoImage(file="images/hang5.png"),
          PhotoImage(file="images/hang6.png"), PhotoImage(
              file="images/hang7.png"), PhotoImage(file="images/hang8.png"),
          PhotoImage(file="images/hang9.png"), PhotoImage(file="images/hang10.png"), PhotoImage(file="images/hang11.png")]

img_lbl = Label(win, bg='#f4ac60')
img_lbl.grid(row=0, column=0, columnspan=2, padx=10, pady=40)

lbl_word = StringVar()
word_label = Label(win, textvariable=lbl_word,
                   font=('consolas 24 bold'), bg='#f4ac60')
word_label.grid(row=0, column=3, columnspan=2, padx=10)

create_keyboard(win)

Button(win, text="New\nGame", command=lambda: new_game(), font=(
    "Helvetica 10 bold"), bg='#f4ac60').grid(row=7, column=8, sticky="nsew")

# Button(win, text="Menu", command=lambda: return_to_main_menu(menu_window, hangman_window), - hangman_window is not defined instead use win to redirect to main window
Button(win, text="Menu", command=lambda: return_to_main_menu(menu_window, win), # replaced hangman_window with win
       font=("Helvetica 10 bold"), bg='#f4ac60').grid(row=7, column=9, sticky="nsew")
random_Hint = StringVar()
print(random_Hint)
hint_label = Label(win, textvariable=random_Hint,
                   font=('consolas 15 bold'), bg='#f4ac60')
hint_label.grid(row=0, column=6)

for i in range(9)[1:10]:
    win.grid_rowconfigure(i, weight=1,  uniform=1)

new_game()

win.mainloop()