class BoardClass:


    def __init__(self, username: str = "", second_username: str = ""):
        """Make a Board.

        Args:
            username: the player's name.
            lastTurnPlayed: the name of the player who moved last turn.
            wins: the number of wins the player has.
            ties: the number of ties the player has.
            losses: the number of losses the player has.

        """
        self.setUsername(username)
        self.setSecondUsername(second_username)
        self.last_turn_player = ""
        self.setWins(0)
        self.setTies(0)
        self.setLosses(0)
        self.numberOfGamesPlayed = 0
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]


    def setUsername(self, username: str):
        """Set the name of the player.
        
        Args:
            username: the player's name.
        """
        self.username = username
    

    def setSecondUsername(self, second_username: str):
        """Set the name of the second player.
        
        Args:
            second_username: the second player's name.
        """
        self.second_username = second_username


    def setWins(self, wins: int):
        """Set the number of wins the player has.
        
        Args:
            wins: the number of wins the player has.
        """
        self.wins = wins


    def setTies(self, ties: int):
        """Set the number of ties the player has.
        
        Args:
            ties: the number of ties the player has.
        """
        self.ties = ties


    def setLosses(self, losses: int):
        """Set the number of losses the player has.
        
        Args:
            losses: the number of losses the player has.
        """
        self.losses = losses


    def checkValidMove(self, move_coords):
        row = int(move_coords[0])
        column = int(move_coords[1])

        if self.board[row][column] == '-':
            return True

        return False
    

    def updateGamesPlayed(self):
        if self.board == [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]:
            self.numberOfGamesPlayed += 1


    def resetGameBoard(self):
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    

    def updateGameBoard(self, move_and_symbol):
        symbol_used = str(move_and_symbol[-1])
        row_move = int(move_and_symbol[0])
        col_move = int(move_and_symbol[1])
        self.board[row_move][col_move] = symbol_used


    def isWinner(self, move_info, player_symbol):
        symbol_used = move_info[-1]
        colCounter = 0
        for row in self.board: #Checks rows
            if row == [symbol_used, symbol_used, symbol_used]:
                if symbol_used == player_symbol:
                    self.wins += 1
                else:
                    self.losses += 1
                return True

        for i in range(3): #Checks columns
            for j in range(3):
                if self.board[j][i] == symbol_used:
                    colCounter += 1
            if colCounter == 3:
                if symbol_used == player_symbol:
                    self.wins += 1
                else:
                    self.losses += 1
                return True
            colCounter = 0

        if self.board[0][0] == symbol_used and self.board[1][1] == symbol_used and self.board[2][2] == symbol_used: #Checks first diagonal
            if symbol_used == player_symbol:
                self.wins += 1
            else:
                self.losses += 1
            return True
        if self.board[0][2] == symbol_used and self.board[1][1] == symbol_used and self.board[2][0] == symbol_used: #Checks second diagonal
            if symbol_used == player_symbol:
                self.wins += 1
            else:
                self.losses += 1
            return True


    def boardIsFull(self):
        fullBoard = True
        for row in self.board:
            for column in row:
                if column == "-":
                    fullBoard = False
        return fullBoard
        

    def printBoard(self):
        print(self.board[0][0], self.board[0][1], self.board[0][2], '\n') #prints gameboard after player 2 moves
        print(self.board[1][0], self.board[1][1], self.board[1][2], '\n')
        print(self.board[2][0], self.board[2][1], self.board[2][2], '\n')


    def boardCondition(self, move_Info, symbol):
        ifWinner = self.isWinner(move_Info, symbol) #Checks if P1 is winner 'o' <== PLAYER 2 SYMBOL
        fullBoard = self.boardIsFull() #Checks if board is full

        return ifWinner, fullBoard


    def computeStats(self):
        return self.username, self.second_username, self.numberOfGamesPlayed, self.wins, self.ties, self.losses