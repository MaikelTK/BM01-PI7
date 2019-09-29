### SETUP ###
import random
from tkinter import *
from tkinter import messagebox
tk = Tk()
tk.title('Tic Tac Toe')


game_End = False
##Field values
Field = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
remaining_moves = 9
Score_X = 0
Score_O = 0
winner = ' '

##Reset game board
def resetBoard():
    global Field
    global Score_O
    global Score_X
    global winner
    global remaining_moves

    ##Give points to winner
    if winner == 'O':
        Score_O += 1
    elif winner == 'X':
        Score_X += 1

    ##Clear gameboard
    Field = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    winner = ' '
    remaining_moves = 9
    ##Redraw gameboard
    loadBoard()


##Human player action
def buttonClick(button):
    global Field
    global remaining_moves

    print(Field)
    if Field[button] == ' ':
        Field[button] = 'O'
        remaining_moves -= 1
        loadBoard()
        checkGameEnd()

        #call AI turn after player made a move
        ai_Turn()


##AI action
def ai_Turn():
    global Field
    global remaining_moves
    valid_move = False

    if remaining_moves > 0:
        while not valid_move:
            randomButton = random.randint(0, 8)
            if Field[randomButton] == ' ':
                Field[randomButton] = 'X'
                remaining_moves -= 1
                valid_move = True

    loadBoard()
    checkGameEnd()
    return


##Check if winconditions are met
def checkGameEnd():
    global game_End
    global winner
    global remaining_moves

    ##Winconditions O
    if (Field[0] == 'O' and Field[1] == 'O' and Field[2] == 'O' or #horizontal_1
        Field[3] == 'O' and Field[4] == 'O' and Field[5] == 'O' or #horizontal_2
        Field[6] == 'O' and Field[7] == 'O' and Field[8] == 'O' or #horizontal_3
        Field[0] == 'O' and Field[3] == 'O' and Field[6] == 'O' or #vertical_1
        Field[1] == 'O' and Field[4] == 'O' and Field[7] == 'O' or #vertical_2
        Field[2] == 'O' and Field[5] == 'O' and Field[8] == 'O' or #vertical_3
        Field[0] == 'O' and Field[4] == 'O' and Field[8] == 'O' or #diagonal_1
        Field[2] == 'O' and Field[4] == 'O' and Field[6] == 'O'  #diagonal_2
        ):
        winner = 'O'
        messagebox.showinfo('Game End', 'Payer O Won!')
        game_End = True

    ##Winconditions X
    elif (Field[0] == 'X' and Field[1] == 'X' and Field[2] == 'X' or #horizontal_1
            Field[3] == 'X' and Field[4] == 'X' and Field[5] == 'X' or #horizontal_2
            Field[6] == 'X' and Field[7] == 'X' and Field[8] == 'X' or #horizontal_3
            Field[0] == 'X' and Field[3] == 'X' and Field[6] == 'X' or #vertical_1
            Field[1] == 'X' and Field[4] == 'X' and Field[7] == 'X' or #vertical_2
            Field[2] == 'X' and Field[5] == 'X' and Field[8] == 'X' or #vertical_3
            Field[0] == 'X' and Field[4] == 'X' and Field[8] == 'X' or #diagonal_1
            Field[2] == 'X' and Field[4] == 'X' and Field[6] == 'X'  #diagonal_2
            ):
        winner = 'X'
        messagebox.showinfo('Game End', 'Payer X Won')
        game_End = True

    #GameTie
    elif remaining_moves == 0 and winner == ' ':
        game_End = True
        messagebox.showinfo('Game End', 'Game Tie!')

    if game_End == True:
        resetBoard()
        game_End = False


##Define and draw the gameboard
def loadBoard():
    #Labels
    label1 = Label(tk, text="O = Human Player", anchor='w', font=20, fg='black', height=2, width=18)
    label2 = Label(tk, text="X = AI Player", anchor='w', font=20, fg='black', height=2, width=18)
    label3 = Label(tk, text="Score O = " + str(Score_O), anchor='w', font=20, fg='black', height=2, width=18)
    label4 = Label(tk, text="Score X = " + str(Score_X), anchor='w', font=20, fg='black', height=2, width=18)

    #Define buttons
    button0 = Button(tk, text='New Game', font='20', bg='gray', height=2, width=18, command=lambda: resetBoard())
    button1 = Button(tk, text=Field[0], font='20', bg='white', height=7, width=18, command=lambda: buttonClick(0))
    button2 = Button(tk, text=Field[1], font='20', bg='white', height=7, width=18, command=lambda: buttonClick(1))
    button3 = Button(tk, text=Field[2], font='20', bg='white', height=7, width=18, command=lambda: buttonClick(2))
    button4 = Button(tk, text=Field[3], font='20', bg='white', height=7, width=18, command=lambda: buttonClick(3))
    button5 = Button(tk, text=Field[4], font='20', bg='white', height=7, width=18, command=lambda: buttonClick(4))
    button6 = Button(tk, text=Field[5], font='20', bg='white', height=7, width=18, command=lambda: buttonClick(5))
    button7 = Button(tk, text=Field[6], font='20', bg='white', height=7, width=18, command=lambda: buttonClick(6))
    button8 = Button(tk, text=Field[7], font='20', bg='white', height=7, width=18, command=lambda: buttonClick(7))
    button9 = Button(tk, text=Field[8], font='20', bg='white', height=7, width=18, command=lambda: buttonClick(8))

    #Draw grid with
    label1.grid(row=1, column=0)
    label2.grid(row=2, column=0)
    label3.grid(row=1, column=1)
    label4.grid(row=2, column=1)
    button0.grid(row=1, column=2)
    button1.grid(row=4, column=0)
    button2.grid(row=4, column=1)
    button3.grid(row=4, column=2)
    button4.grid(row=5, column=0)
    button5.grid(row=5, column=1)
    button6.grid(row=5, column=2)
    button7.grid(row=6, column=0)
    button8.grid(row=6, column=1)
    button9.grid(row=6, column=2)


loadBoard()
tk.mainloop()


