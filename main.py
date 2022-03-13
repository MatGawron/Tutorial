# import re
import tkinter as ttk
from tkinter import *
import messagebox


class Model:
    global root
    count = 0
    Empty = 0
    Gracz_1 = 1
    Gracz_2 = 2


def destruct():
    global root, winnerWindow
    root.destroy()
    winnerWindow.destroy()


def displayWinner(winner):
    global root, winnerWindow, ID
    winnerWindow = Tk()
    winnerWindow.title("Winner Window")
    winnerWindow.configure(bg="Black")
    l1 = Label(winnerWindow, text="THE WINNER IS: ", font=("COMIC SANS MS", 15), bg="Black", fg="White")
    l1.pack()
    l2 = Label(winnerWindow, text=winner, font=("COMIC SANS MS", 15), bg="Black", fg="White")
    l2.pack()
    bproceed = Button(winnerWindow, text="Proceed", font=("COMIC SANS MS", 10, "bold"), command=destruct)
    bproceed.pack()


def checkWinner():
    global count, board
    if (board[0][0] == board[0][1] == board[0][2] == "X" or board[1]
        [0] == board[1][1] == board[1][2] == "X" or board[2][0] == board[2]
        [1] == board[2][2] == "X" or board[0][0] == board[1][0] == board[2]
        [0] == "X" or board[0][1] == board[1][1] == board[2][1] == "X" or
            board[0][2] == board[1][2] == board[2][2] == "X" or
            board[0][0] == board[1][1] == board[2][2] == "X" or board[0]
            [2] == board[1][1] == board[2][0] == "X"):
        displayWinner("Player X")
    elif (board[0][0] == board[0][1] == board[0][2] == "O" or board[1]
          [0] == board[1][1] == board[1][2] == "O" or board[2][0]
          == board[2][1] == board[2][2] == "O" or
          board[0][0] == board[1][0] == board[2][0] == "O" or board[0]
          [1] == board[1][1] == board[2][1] == "O" or board[0]
          [2] == board[1][2] == board[2][2] == "O" or board[0]
          [0] == board[1][1] == board[2][2] == "O" or board[0]
          [2] == board[1][1] == board[2][0] == "O"):
        displayWinner("Player O")
    elif count == 9:
        displayWinner("NONE! IT IS A TIE!")


def changeVal(button, boardValRow, boardValCol):
    global count

    # Checking if button is available
    if button["text"] == "":
        if count % 2 == 0:
            button["text"] = "X"
            l1 = Label(root, text="PLAYER: 2(O)", height=3, font=("COMIC SANS MS", 10, "bold"),
            bg="white").grid(row=0, column=0)
            board[boardValRow][boardValCol] = "X"
        else:
            button["text"] = "O"
            l1 = Label(root, text="PLAYER: 1(X)", height=3, font=("COMIC SANS MS", 10, "bold"),
            bg="white").grid(row=0, column=0)
            board[boardValRow][boardValCol] = "O"
        count = count + 1
        if count >= 5:
            checkWinner()
    else:
        messagebox.showerror("Error", "This box already has a value!")


class View(ttk.Frame):
    root = ttk.Tk()
    # setting window tittle
    root.title("Kółko i krzyżyk")
    # setting default window size
    root.geometry("318x375")
    root.configure(bg="light yellow")

    count = 0
    global board
    board = [["", "", ""],
             ["", "", ""],
             ["", "", ""]]

    l1 = Label(root, text="PLAYER: 1(X)", height=3, font=("Arial", 8, "bold"), bg="white")
    l1.grid(row=0, column=2)
    # Create Buttons
    buttons = StringVar()

    b1 = Button(root, text="", height=4, width=8, bg="light yellow", activebackground="peachpuff", fg="black",
                font="Times 15 bold", command=lambda: changeVal(b1, 0, 0))
    b2 = Button(root, text="", height=4, width=8, bg="light yellow", activebackground="peachpuff", fg="black",
                font="Times 15 bold", command=lambda: changeVal(b2, 0, 1))
    b3 = Button(root, text="", height=4, width=8, bg="light yellow", activebackground="peachpuff", fg="black",
                font="Times 15 bold", command=lambda: changeVal(b3, 0, 2))
    b4 = Button(root, text="", height=4, width=8, bg="light yellow", activebackground="peachpuff", fg="black",
                font="Times 15 bold", command=lambda: changeVal(b4, 1, 0))
    b5 = Button(root, text="", height=4, width=8, bg="light yellow", activebackground="peachpuff", fg="black",
                font="Times 15 bold", command=lambda: changeVal(b5, 1, 1))
    b6 = Button(root, text="", height=4, width=8, bg="light yellow", activebackground="peachpuff", fg="black",
                font="Times 15 bold", command=lambda: changeVal(b6, 1, 2))
    b7 = Button(root, text="", height=4, width=8, bg="light yellow", activebackground="peachpuff", fg="black",
                font="Times 15 bold", command=lambda: changeVal(b7, 2, 0))
    b8 = Button(root, text="", height=4, width=8, bg="light yellow", activebackground="peachpuff", fg="black",
                font="Times 15 bold", command=lambda: changeVal(b8, 2, 1))
    b9 = Button(root, text="", height=4, width=8, bg="light yellow", activebackground="peachpuff", fg="black",
                font="Times 15 bold", command=lambda: changeVal(b9, 2, 2))

    b1.grid(row=2, column=0)
    b2.grid(row=2, column=1)
    b3.grid(row=2, column=2)
    b4.grid(row=3, column=0)
    b5.grid(row=3, column=1)
    b6.grid(row=3, column=2)
    b7.grid(row=4, column=0)
    b8.grid(row=4, column=1)
    b9.grid(row=4, column=2)

    exitButton = Button(root, text="exit", height=1, width=3, bg="white", activebackground="peachpuff", fg="black",
                        font="Arial 9", command=lambda: quit())
    exitButton.grid(row=0, column=0)

    def quit(self):
        global root
        msg = messagebox.askquestion("Confirm", "Are you want to Quit? You still have chances!")
        if msg == "yes":
            root.destroy()


    root.mainloop()
