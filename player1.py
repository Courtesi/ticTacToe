from tkinter import *
from tkinter import ttk
import gameboard as gb
import socket

class Interface():
    GameBoard = 0
    def __init__(self):
        self.GameBoard = gb.BoardClass("","")

        #CANVAS SETUP WITH TKVARIABLES INITIALIZED
        self.WindowSetup()
        self.initTkVariables()

        #IP ADDRESS, PORT, AND USERNAME WITH ENTER BUTTON
        self.priortogamedatainfo()

        #ACTUAL GUI BOARD
        self.BoardInGUI()

    def WindowSetup(self):
        self.root = Tk()
        self.frame = ttk.Frame(self.root, padding = 10)
        self.frame.grid()
        self.root.title('Player 1')

    def initTkVariables(self):
        self.ip_address_string = StringVar()
        self.port_int = StringVar()
        self.username_string = StringVar()

    def priortogamedatainfo(self):
        self.ip_address = ttk.Entry(self.frame,textvariable = self.ip_address_string).grid(column=1, row=0)
        self.port = ttk.Entry(self.frame, textvariable = self.port_int).grid(column=1, row=1)
        ttk.Label(self.frame, text = "IP Address").grid(column = 0, row = 0)
        ttk.Label(self.frame, text = "Port").grid(column = 0, row = 1)

        ttk.Label(self.frame, text = "Username").grid(column = 0, row = 2)
        self.username = ttk.Entry(self.frame, textvariable = self.username_string).grid(column = 1, row = 2)
        self.submit_button = ttk.Button(self.frame, command=self.SubmitFunction, text = "Enter")
        self.submit_button.grid(column=1, row=3)

    def SubmitFunction(self):
        port_number = int(self.port_int.get())
        self.connectSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connectSocket.connect((self.ip_address_string.get(), port_number))

        player_username = str(self.username_string.get())
        self.connectSocket.send(bytes(player_username, 'utf-8')) #Sends P1's username

        self.ip_address_string = ""
        self.port_int = StringVar()
        self.username_string = ""

        player2info = self.connectSocket.recv(1024) #Receives P1 move
        player2username = player2info.decode('ascii')

        self.GameBoard.updateGamesPlayed()
        self.GameBoard.username = player_username
        self.GameBoard.second_username = player2username

        self.submit_button["state"] = "disabled"

        self.turn_status = ttk.Label(self.frame, text = "Your Turn")
        self.turn_status.grid(column = 0, row = 4)

    def BoardInGUI(self):
        self.button_00 = ttk.Button(self.frame, command = lambda: self.ButtonFunction("00"), text = "")
        self.button_00.grid(column=2, row=4)

        self.button_01 = ttk.Button(self.frame, command = lambda: self.ButtonFunction("01"), text = "")
        self.button_01.grid(column=2, row=5)

        self.button_02 = ttk.Button(self.frame, command = lambda: self.ButtonFunction("02"), text = "")
        self.button_02.grid(column=2, row=6)

        self.button_10 = ttk.Button(self.frame, command = lambda: self.ButtonFunction("10"), text = "")
        self.button_10.grid(column=3, row=4)

        self.button_11 = ttk.Button(self.frame, command = lambda: self.ButtonFunction("11"), text = "")
        self.button_11.grid(column=3, row=5)

        self.button_12 = ttk.Button(self.frame, command = lambda: self.ButtonFunction("12"), text = "")
        self.button_12.grid(column=3, row=6)

        self.button_20 = ttk.Button(self.frame, command = lambda: self.ButtonFunction("20"), text = "")
        self.button_20.grid(column=4, row=4)

        self.button_21 = ttk.Button(self.frame, command = lambda: self.ButtonFunction("21"), text = "")
        self.button_21.grid(column=4, row=5)

        self.button_22 = ttk.Button(self.frame, command = lambda: self.ButtonFunction("22"), text = "")
        self.button_22.grid(column=4, row=6)

    def ButtonFunction(self, move):
        if move == "00":
            #CHANGES TEXT OF BUTTON TO LETTER OF PLAYER
            self.button_00["text"] = "X"

            #LOCKS BUTTON
            self.button_00["state"] = "disabled"

            #UPDATES IDLETASKS?
            self.root.update_idletasks()

            self.SubButtonFunction(move)

        elif move == "01":
            #CHANGES TEXT OF BUTTON TO LETTER OF PLAYER
            self.button_01["text"] = "X"

            #LOCKS BUTTON
            self.button_01["state"] = "disabled"

            #UPDATES IDLETASKS?
            self.root.update_idletasks()

            self.SubButtonFunction(move)

        elif move == "02":
            #CHANGES TEXT OF BUTTON TO LETTER OF PLAYER
            self.button_02["text"] = "X"

            #LOCKS BUTTON
            self.button_02["state"] = "disabled"

            #UPDATES IDLETASKS?
            self.root.update_idletasks()

            self.SubButtonFunction(move)

        elif move == "10":
            #CHANGES TEXT OF BUTTON TO LETTER OF PLAYER
            self.button_10["text"] = "X"

            #LOCKS BUTTON
            self.button_10["state"] = "disabled"

            #UPDATES IDLETASKS?
            self.root.update_idletasks()

            self.SubButtonFunction(move)

        elif move == "11":
            #CHANGES TEXT OF BUTTON TO LETTER OF PLAYER
            self.button_11["text"] = "X"

            #LOCKS BUTTON
            self.button_11["state"] = "disabled"

            #UPDATES IDLETASKS?
            self.root.update_idletasks()

            self.SubButtonFunction(move)

        elif move == "12":
            #CHANGES TEXT OF BUTTON TO LETTER OF PLAYER
            self.button_12["text"] = "X"

            #LOCKS BUTTON
            self.button_12["state"] = "disabled"

            #UPDATES IDLETASKS?
            self.root.update_idletasks()

            self.SubButtonFunction(move)

        elif move == "20":
            #CHANGES TEXT OF BUTTON TO LETTER OF PLAYER
            self.button_20["text"] = "X"

            #LOCKS BUTTON
            self.button_20["state"] = "disabled"

            #UPDATES IDLETASKS?
            self.root.update_idletasks()

            self.SubButtonFunction(move)

        elif move == "21":
            #CHANGES TEXT OF BUTTON TO LETTER OF PLAYER
            self.button_21["text"] = "X"

            #LOCKS BUTTON
            self.button_21["state"] = "disabled"

            #UPDATES IDLETASKS?
            self.root.update_idletasks()

            self.SubButtonFunction(move)

        elif move == "22":
            #CHANGES TEXT OF BUTTON TO LETTER OF PLAYER
            self.button_22["text"] = "X"

            #LOCKS BUTTON
            self.button_22["state"] = "disabled"

            #UPDATES IDLETASKS?
            self.root.update_idletasks()

            self.SubButtonFunction(move)


    def SubButtonFunction(self, move):
        #CHANGES TURN STATUS BOX INTO OPPONENT'S ONCE YOU HIT BUTTON
        self.turn_status["text"] = "Opponent's Turn"
        self.root.update_idletasks()

        #UPDATES GAMEBOARD
        move += "x"
        self.GameBoard.updateGameBoard(move)
        
        #SENDS MOVE
        self.connectSocket.send(bytes(move, 'utf-8'))

        #CHECKS MOVE CONDITION IN BOARD
        check_win, check_tie = self.GameBoard.boardCondition(move, 'x')

        #WILL RETURN INT VALUE: [0, 1, 2] 0: CONTINUES, 1: RESETS LOOP AND MAKES P2 LISTEN, 2: QUITS THE GAME AND RETURNS STATS
        status_of_board_to_continue = self.CheckStatusAndMakeDecision(check_win, check_tie)

        if status_of_board_to_continue:
            self.OpponentMoveResponse()

    def OpponentMoveResponse(self):
        #LISTENS FOR MOVE
            player1info = self.connectSocket.recv(1024)
            player1move = player1info.decode('ascii') #NEEDS TO SEND MOVE IN FORM OF "11X"

            #CHANGES TURN STATUS BOX BACK INTO YOURS ONCE RECEIVES MOVE
            self.turn_status["text"] = "Your Turn"

            #LISTENING BUTTON FUNCTION
            self.ListeningButtonFunction(player1move)

            #UPDATES OPPONENT MOVE ON GAMEBOARD
            self.GameBoard.updateGameBoard(player1move)

            #CHECKS OPPONENT'S MOVE CONDITION IN BOARD
            check_win, check_tie = self.GameBoard.boardCondition(player1move, 'x')
            self.CheckStatusAndMakeDecision(check_win, check_tie)

    def ListeningButtonFunction(self, opponent_move):

        coordinate = opponent_move[0] + opponent_move[1]

        if coordinate == "00":
            self.button_00["text"] = "O"
            self.button_00["state"] = "disabled"
            self.root.update_idletasks()

        elif coordinate == "01":
            self.button_01["text"] = "O"
            self.button_01["state"] = "disabled"
            self.root.update_idletasks()

        elif coordinate == "02":
            self.button_02["text"] = "O"
            self.button_02["state"] = "disabled"
            self.root.update_idletasks()

        elif coordinate == "10":
            self.button_10["text"] = "O"
            self.button_10["state"] = "disabled"
            self.root.update_idletasks()

        elif coordinate == "11":
            self.button_11["text"] = "O"
            self.button_11["state"] = "disabled"
            self.root.update_idletasks()

        elif coordinate == "12":
            self.button_12["text"] = "O"
            self.button_12["state"] = "disabled"
            self.root.update_idletasks()

        elif coordinate == "20":
            self.button_20["text"] = "O"
            self.button_20["state"] = "disabled"
            self.root.update_idletasks()

        elif coordinate == "21":
            self.button_21["text"] = "O"
            self.button_21["state"] = "disabled"
            self.root.update_idletasks()

        elif coordinate == "22":
            self.button_22["text"] = "O"
            self.button_22["state"] = "disabled"
            self.root.update_idletasks()


    def CheckStatusAndMakeDecision(self, check_win, check_tie) -> int:
        continue_the_loop = True

        if check_win:
            self.LockAllButtons()

            self.play_again_label = ttk.Label(self.frame, text = "Game ended. Do you want to play again?")
            self.play_again_label.grid(column = 6, row = 7)

            self.play_again_button_yes = ttk.Button(self.frame, command = lambda: self.DecisionToPlayAgainButton("Yes"), text = "Yes")
            self.play_again_button_yes.grid(column=6, row=8)

            self.play_again_button_no = ttk.Button(self.frame, command = lambda: self.DecisionToPlayAgainButton("No"), text = "No")
            self.play_again_button_no.grid(column=6, row=9)

            continue_the_loop = False

        elif check_tie:
            self.LockAllButtons()

            self.GameBoard.ties += 1

            self.play_again_label = ttk.Label(self.frame, text = "Game ended. Do you want to play again?")
            self.play_again_label.grid(column = 6, row = 7)

            self.play_again_button_yes = ttk.Button(self.frame, command = lambda: self.DecisionToPlayAgainButton("Yes"), text = "Yes")
            self.play_again_button_yes.grid(column=6, row=8)

            self.play_again_button_no = ttk.Button(self.frame, command = lambda: self.DecisionToPlayAgainButton("No"), text = "No")
            self.play_again_button_no.grid(column=6, row=9)

            continue_the_loop = False

        return continue_the_loop


    def DecisionToPlayAgainButton(self, decision):
        if decision == "Yes":
            self.connectSocket.send(bytes("Play Again", 'utf-8'))
            self.GameBoard.resetGameBoard()
            self.GameBoard.updateGamesPlayed()
            self.turn_status["text"] = "Your Turn"

            self.ButtonStateReset()

            self.root.update_idletasks()

            #DESTROYS DECISION BUTTONS
            self.play_again_button_yes.destroy()
            self.play_again_button_no.destroy()
            self.play_again_label.destroy()


        elif decision == "No":
            self.connectSocket.send(bytes("Fun Times", 'utf-8'))
            self.GameFinish()
            self.play_again_button_yes.destroy()
            self.play_again_button_no.destroy()
            self.play_again_label.destroy()


    def ButtonStateReset(self):
        #UNLOCKS BUTTONS
        self.button_00["state"] = "normal"
        self.button_01["state"] = "normal"
        self.button_02["state"] = "normal"
        self.button_10["state"] = "normal"
        self.button_11["state"] = "normal"
        self.button_12["state"] = "normal"
        self.button_20["state"] = "normal"
        self.button_21["state"] = "normal"
        self.button_22["state"] = "normal"

        #CLEARS TEXT OF BUTTONS
        self.button_00["text"] = ""
        self.button_01["text"] = ""
        self.button_02["text"] = ""
        self.button_10["text"] = ""
        self.button_11["text"] = ""
        self.button_12["text"] = ""
        self.button_20["text"] = ""
        self.button_21["text"] = ""
        self.button_22["text"] = ""


    def LockAllButtons(self):
        self.button_00["state"] = "disabled"
        self.button_01["state"] = "disabled"
        self.button_02["state"] = "disabled"
        self.button_10["state"] = "disabled"
        self.button_11["state"] = "disabled"
        self.button_12["state"] = "disabled"
        self.button_20["state"] = "disabled"
        self.button_21["state"] = "disabled"
        self.button_22["state"] = "disabled"


    def GameFinish(self):
        stat, stat1, stat2, stat3, stat4, stat5 = self.GameBoard.computeStats()
        ttk.Label(self.frame, text = "Your name: " + stat).grid(column = 5, row = 0)
        ttk.Label(self.frame, text = "Your opponent: " + stat1).grid(column = 5, row = 1)
        ttk.Label(self.frame, text = "Games Played: " + str(stat2)).grid(column = 5, row = 2)
        ttk.Label(self.frame, text = "Wins: " + str(stat3)).grid(column = 5, row = 3)
        ttk.Label(self.frame, text = "Ties: " + str(stat4)).grid(column = 5, row = 4)
        ttk.Label(self.frame, text = "Losses: " + str(stat5)).grid(column = 5, row = 5)

        self.LockAllButtons()

        self.root.update_idletasks()


    def Player1TotalFunction(self):
        self.root.mainloop()

if __name__ == "__main__":
    Interface().Player1TotalFunction()