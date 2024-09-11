import tkinter

def set_title(row, column):
    global curr_player, game_over
    
    if game_over:
        return

    if board[row][column]["text"] != "":
        return
    
    board[row][column]["text"] = curr_player

    if curr_player == playerO:
        curr_player = playerX
    else:
        curr_player = playerO

    label["text"] = curr_player + "'s turn"
    
    # Check for a winner
    check_winner()

def check_winner():
    global turns, game_over
    turns += 1

    # Horizontal check
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"] + " Wins !!!", foreground=color_yellow)
            for column in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_gray)
            game_over = True
            return
    
    # Vertical check
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"] + " Wins !!!", foreground=color_yellow)
            for row in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_gray)
            game_over = True
            return
    
    # Diagonal check
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"] + " Wins !!!", foreground=color_yellow)
        for i in range(3):
            board[i][i].config(foreground=color_yellow, background=color_light_gray)
        game_over = True
        return

    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"] + " Wins !!!", foreground=color_yellow)
        for i in range(3):
            board[i][2-i].config(foreground=color_yellow, background=color_light_gray)
        game_over = True
        return
    
    # Check for a draw
    if turns == 9:
        label.config(text="Draw !!!", foreground=color_yellow)
        game_over = True

def new_game():
    global game_over, turns
    game_over = False
    turns = 0
    label.config(text=curr_player+"'s turn", foreground="white")
    
    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_blue, background=color_gray)\

def quit():
    window.quit()

# Game setup
playerX = "X"
playerO = "O"
curr_player = playerX
board = [[0,0,0], 
         [0,0,0], 
         [0,0,0]]

color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"
color_light_gray = "#646464"

turns = 0 
game_over = False

# Window
window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=curr_player + "'s turn", font=("Consolas", 20), background=color_gray, foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"), 
                                            background=color_gray, foreground=color_blue, width=4, height=1,
                                            command=lambda row=row, column=column: set_title(row, column))
        board[row][column].grid(row=row+1, column=column)

button = tkinter.Button(frame, text="Restart", font=("Consolas", 20), background=color_gray,
                        foreground="white", command=new_game)
button.grid(row=4, column=0, columnspan=2, sticky="we")

button = tkinter.Button(frame, text="Quit", font=("Consolas", 20), background=color_gray,
                        foreground="white", command=quit)
button.grid(row=4, column=2, columnspan=1, sticky="we" )

frame.pack()
# Center app
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))
# Format (X,Y,Z)
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
window.mainloop()
