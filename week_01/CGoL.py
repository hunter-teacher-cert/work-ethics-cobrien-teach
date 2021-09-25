import board

def generateNextBoard(myBoard):
    numRow = myBoard.height()
    numCol = myBoard.width()
    newBoard = board.Board(numRow,numCol)
    print("type of newBoard: " + str(type(newBoard)))
    for row in range(numRow):
        for col in range(numCol):
            newCell = myBoard.getNextGenCell(row,col)
            newBoard.setCell(row,col,newCell)
    return newBoard

myBoard = board.Board(25,25)
myBoard.setCell(10, 10, 'X');
myBoard.setCell(10, 11, 'X');
myBoard.setCell(7, 8, 'X');
myBoard.setCell(9,10,'X');
myBoard.setCell(9,11,'X');
myBoard.setCell(8,12,'X');
myBoard.setCell(5,11,'X');
myBoard.setCell(5,10,'X');
myBoard.setCell(6,11,'X');
myBoard.setCell(6,10,'X');
print(myBoard)
newBoard = generateNextBoard(myBoard)

print(newBoard)
