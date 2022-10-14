from tkinter import *
from tkinter import ttk
import gameboard as gb
import socket

class Interface:
    #Defining Gameboard Class Variable
    GameBoard = 0

    def __init__(self):
        self.GameBoard = gb.BoardClass("", "")

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
        self.root.title('Player 2')

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

    def SubmitFunction(self) -> str:
        port_number = int(self.port_int.get())

        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.bind((self.ip_address_string.get(), port_number))
        self.serverSocket.listen(1)

        self.p1connectSocket, player1Address = self.serverSocket.accept()

        player1info = self.p1connectSocket.recv(1024) #Receives P1 move
        player1username = player1info.decode('ascii')

        player_username = str(self.username_string.get())
        self.p1connectSocket.send(bytes(player_username, 'utf-8')) #SENDS USERNAME

        self.GameBoard.username = player_username
        self.GameBoard.second_username = player1username

        self.ip_address_string = ""
        self.port_int = StringVar()
        self.username_string = ""

        self.turn_status = ttk.Label(self.frame, text = "Opponent's Turn")
        self.turn_status.grid(column = 0, row = 4)

        self.root.update_idletasks()

        self.submit_button["state"] = "disabled"
        self.GameBoard.updateGamesPlayed()

        player1info = self.p1connectSocket.recv(1024) #Receives P1 move
        player1move = player1info.decode('ascii')

        self.turn_status["text"] = "Your Turn"

        self.root.update_idletasks()

        #LISTENING BUTTON FUNCTION
        self.ListeningButtonFunction(player1move)

        #UPDATES OPPONENT MOVE ON GAMEBOARD
        self.GameBoard.updateGameBoard(player1move)


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

        # if move is avalible : self.hostboard.checkValidMove()

        
        if move == "00":
            #CHANGES TEXT OF BUTTON TO LETTER OF PLAYER
            self.button_00["text"] = "O"

            #LOCKS BUTTON
            self.button_00["state"] = "disabled"

            #UPDATES IDLETASKS?
            self.root.update_idletasks()

            self.SubButtonFunction(move)
        elif move == "01":
            #CHANGES TEXT OF BUTTON TO LETTER OF PLAYER
            self.button_01["text"] = "O"

            #LOCKS BUTTON
            self.button_01["state"] = "disabled"

            #UPDATES IDLETASKS?
            self.root.update_idletasks()

            self.SubButtonFunction(move)

        elif move == "02":
            #CHANGES TEXT OF BUTTON TO LETTER OF PLAYER
            self.button_02["text"] = "O"

            #LOCKS BUTTON
            self.button_02["state"] = "disabled"

            #UPDATES IDLETASKS?
            self.root.update_idletasks()

            self.SubButtonFunction(move)

        elif move == "10":
            #CHANGES TEXT OF BUTTON TO LETTER OF PLAYER
            self.button_10["text"] = "O"

            #LOCKS BUTTON
            self.button_10["state"] = "disabled"

            #UPDATES IDLETASKS?
            self.root.update_idletasks()

            self.SubButtonFunction(move)

        elif move == "11":
            #CHANGES TEXT OF BUTTON TO LETTER OF PLAYER
            self.button_11["text"] = "O"

            #LOCKS BUTTON
            self.button_11["state"] = "disabled"

            #UPDATES IDLETASKS?
            self.root.update_idletasks()

            self.SubButtonFunction(move)

        elif move == "12":
            #CHANGES TEXT OF BUTTON TO LETTER OF PLAYER
            self.button_12["text"] = "O"

            #LOCKS BUTTON
            self.button_12["state"] = "disabled"

            #UPDATES IDLETASKS?
            self.root.update_idletasks()

            self.SubButtonFunction(move)

        elif move == "20":
            #CHANGES TEXT OF BUTTON TO LETTER OF PLAYER
            self.button_20["text"] = "O"

            #LOCKS BUTTON
            self.button_20["state"] = "disabled"

            #UPDATES IDLETASKS?
            self.root.update_idletasks()

            self.SubButtonFunction(move)

        elif move == "21":
            #CHANGES TEXT OF BUTTON TO LETTER OF PLAYER
            self.button_21["text"] = "O"

            #LOCKS BUTTON
            self.button_21["state"] = "disabled"

            #UPDATES IDLETASKS?
            self.root.update_idletasks()

            self.SubButtonFunction(move)

        elif move == "22":
            #CHANGES TEXT OF BUTTON TO LETTER OF PLAYER
            self.button_22["text"] = "O"

            #LOCKS BUTTON
            self.button_22["state"] = "disabled"

            #UPDATES IDLETASKS?
            self.root.update_idletasks()

            self.SubButtonFunction(move)


    def SubButtonFunction(self, move):
        #CHANGES TURN STATUS BOX INTO OPPONENT'S ONCE YOU HIT BUTTON
        self.turn_status["text"] = "Opponent's Turn"
        self.root.update_idletasks()

        self.GameBoard.updateGamesPlayed()
        #UPDATES GAMEBOARD
        move += "o"
        self.GameBoard.updateGameBoard(move)

        #SENDS MOVE
        self.p1connectSocket.send(bytes(move, 'utf-8'))
        
        #CHECKS MOVE CONDITION IN BOARD
        check_win, check_tie = self.GameBoard.boardCondition(move, 'o')

        #WILL RETURN INT VALUE: [0, 1, 2] 0: CONTINUES, 1: RESETS LOOP AND MAKES P2 LISTEN, 2: QUITS THE GAME AND RETURNS STATS
        reset_question = self.CheckStatus(check_win, check_tie)

        if reset_question == 2:
            pass
        else:
            #LISTENS FOR MOVE AND CHECKS IF OPPONENT WON
            status_of_board_to_reset = self.OpponentMoveResponse()

            if status_of_board_to_reset == 1:
                self.OpponentMoveResponse()

    def OpponentMoveResponse(self):
        player1info = self.p1connectSocket.recv(1024) 
        player1move = player1info.decode('ascii') #NEEDS TO SEND MOVE IN FORM OF "11X"

        self.turn_status["text"] = "Your Turn"

        #LISTENING BUTTON FUNCTION
        self.ListeningButtonFunction(player1move)

        #UPDATES OPPONENT MOVE ON GAMEBOARD
        self.GameBoard.updateGameBoard(player1move)

        check_win2, check_tie2 = self.GameBoard.boardCondition(player1move, 'o')

        status_of_board_to_reset = self.CheckStatus(check_win2, check_tie2)

        return status_of_board_to_reset
    

    def ListeningButtonFunction(self, opponent_move):
        
        coordinate = opponent_move[0] + opponent_move[1]

        if coordinate == "00":
            self.button_00["text"] = "X"
            self.button_00["state"] = "disabled"
            self.root.update_idletasks()
        
        elif coordinate == "01":
            self.button_01["text"] = "X"
            self.button_01["state"] = "disabled"
            self.root.update_idletasks()

        elif coordinate == "02":
            self.button_02["text"] = "X"
            self.button_02["state"] = "disabled"
            self.root.update_idletasks()

        elif coordinate == "10":
            self.button_10["text"] = "X"
            self.button_10["state"] = "disabled"
            self.root.update_idletasks()
        
        elif coordinate == "11":
            self.button_11["text"] = "X"
            self.button_11["state"] = "disabled"
            self.root.update_idletasks()
        
        elif coordinate == "12":
            self.button_12["text"] = "X"
            self.button_12["state"] = "disabled"
            self.root.update_idletasks()
        
        elif coordinate == "20":
            self.button_20["text"] = "X"
            self.button_20["state"] = "disabled"
            self.root.update_idletasks()
        
        elif coordinate == "21":
            self.button_21["text"] = "X"
            self.button_21["state"] = "disabled"
            self.root.update_idletasks()
        
        elif coordinate == "22":
            self.button_22["text"] = "X"
            self.button_22["state"] = "disabled"
            self.root.update_idletasks()

    def CheckStatus(self, check_win_p1, check_tie_p1) -> BooleanVar:
        reset_to_listen = 0

        if check_win_p1:
            self.LockAllButtons()

            self.root.update_idletasks()

            p_1_choice = self.p1connectSocket.recv(1024) #Receives P1 decision
            player_1_decision = p_1_choice.decode('ascii')

            if player_1_decision == "Play Again":
                reset_to_listen = 1
                self.GameBoard.resetGameBoard()
                self.GameBoard.updateGamesPlayed()
                self.turn_status["text"] = "Opponent's Turn"

                self.ButtonStateReset()
                
            elif player_1_decision == "Fun Times":
                reset_to_listen = 2
                self.GameFinish()
                

        elif check_tie_p1:
            self.GameBoard.ties += 1
            self.LockAllButtons()

            self.root.update_idletasks()

            p_1_choice = self.p1connectSocket.recv(1024) #Receives P1 decision
            player_1_decision = p_1_choice.decode('ascii')

            if player_1_decision == "Play Again":
                reset_to_listen = 1
                self.GameBoard.resetGameBoard()
                self.GameBoard.updateGamesPlayed()
                self.turn_status["text"] = "Opponent's Turn"

                self.ButtonStateReset()

            elif player_1_decision == "Fun Times":
                reset_to_listen = 2
                self.GameFinish()
        
        return reset_to_listen

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

        self.root.update_idletasks()

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

    def Player2TotalFunction(self):
        self.root.mainloop()

if __name__ == "__main__":
    Interface().Player2TotalFunction()