from random import shuffle, randint #as randomize

def FillTheBoard (rows,cols,TileList):  #insertsvalues into the nice matrix
    Board = []
    for r in range(rows): Board.append([]) 
    for i in range(len(TileList)):
        Board[i//cols].append((MaxLength*" "+str(TileList[i]))[-MaxLength:])        
    return Board

def ShowBoard(): # present puzzle in a nice array
    for i in range(BoardRows):
        print str(YourBoard[i]).replace("'","") # without this replace the empty field would show single quote

def TileLocator(RequestedTile):  #find coordinate of tile with certain number in it
    RequestedTile = ("  " + str(RequestedTile) )[-MaxLength:]
    for row in range(BoardRows):
        if RequestedTile in YourBoard[row]:
            col = YourBoard[row].index(RequestedTile)
            return (row,col)

def MoveNow(TileValue,OldPosition):  #replace empty tile with value of the moved one leaving old field empty
    YourBoard [EmptyTail[0]][EmptyTail[1]] = (MaxLength*" "+ str(TileValue))[-MaxLength:]
    YourBoard [OldPosition[0]][OldPosition[1]] = MaxLength*" "  # Create empty tile in the old position


def ValidMove(MovingTile):  # check if tile can be moved and call moving function
    TilePosition = TileLocator(MovingTile)
    if abs(EmptyTail[0] - TilePosition[0]) + abs(EmptyTail[1] - TilePosition[1]) !=1:  
    ## so total distance on x and y axis is one (so same row one right abobve another or same column, one right next to another
        print "I cannot move " + str(MovingTile) + " select other tile"
    else:
        MoveNow(MovingTile,TilePosition)



print "\n\n\n\n\n\n\n\n\n\nWelcome to the puzzle!"
BoardRows = int(raw_input("Please enter number of rows: "))
BoardCols = int (raw_input("Please enter number of columns: "))
# check if input is fine with try:
BoardContent=range(1,BoardRows*BoardCols)
BoardContent.append(" ")
try:
    MaxLength = len(str(BoardContent[-2]))  #only ntil GUI is ready. 1x1 case gives out of range error - need to specify it in except here.
except:
    MaxLength=1
WinnerBoard = FillTheBoard(BoardRows, BoardCols, BoardContent)
# special cases like 2x2, 1x1, 1xn and nx1
if BoardRows*BoardCols < 2:
    print "\n\n          !!!   Instant Win   !!!\n\n   Yet you still seem like a looser to me...\n\n"
    quit()
elif BoardRows*BoardCols==4:
    EmptySquare = randint(0,2)
    BoardContent.insert(EmptySquare," ")
    BoardContent = BoardContent [:-1]
    if EmptySquare !=2: BoardContent[2:] = [3,2]
    
    
elif min(BoardRows,BoardCols)==1:
    BoardContent.insert(randint (0,BoardRows*BoardCols-2)," ")
    BoardContent = BoardContent [:-1]
    print "\n\nThat's too easy, man..."
else:
    shuffle(BoardContent)
YourBoard = FillTheBoard(BoardRows, BoardCols, BoardContent)





while YourBoard != WinnerBoard:
    print "\n\nThis is your board:\n"
    ShowBoard()
    EmptyTail = TileLocator(" ") # This is after the move. I would rather incorporate it in moving code...
    TileUserWantsToMove = raw_input("Which tile should I move?: ")
    ValidMove(TileUserWantsToMove)

# when you win - this is what you get:
print "\n\n\n\n\n   !!!   C O N G R T U L A T I O N S   !!!\n\n                   You Won!!!\n\n"
raw_input ("\n\n\n\n\n   Please press enter to quit the game.\n\n ")
