class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = self.createNewBoard(self.rows, self.cols)



    def createNewBoard(self,rows, cols):
        row = [' ']*cols
        board = []
        for i in range(rows):
            board.append(row.copy())
        return board

    def countNeighbours(self,row, col):
        sum = 0
        newCell = ' '
        for r in range(row-1,row+2):
            if r>=0 and r<self.height():

                for c in range(col-1, col+2):
                    if c< self.width() and not( r== row and c == col):
                        if self.board[r][c] =='X':
                            sum+=1
        return sum

    def getNextGenCell(self,row, col):
        numNeighbors = self.countNeighbours(row,col)
        if self.getCell(row,col) == 'X':
            if numNeighbors > 3 or numNeighbors < 2:
                newCell = ' '
            else:
                newCell = 'X'
        else:
            if numNeighbors == 3:
                newCell = 'X'
            else:
                newCell = ' '
        return newCell



    def width(self):
        return(self.cols)

    def height(self):
        return(self.rows)

    def getCell(self, row, col):
        return self.board[row][col]

    def setCell(self,row, col,  val):
        self.board[row][col] = val

    def printList(self):
        print(self.board)

    def __str__(self):
        boardView = ''
        for row in self.board:
            rowString = '|'.join(row)
            rowString += '\n'
            boardView += rowString
        return boardView
