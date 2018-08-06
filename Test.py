from Board import *
from Move import *

b = Board(Board.initializeBoard())

notation = ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8",
                "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7",
                "a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6",
                "a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5",
                "a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4",
                "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3",
                "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2",
                "a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]

zipMap = dict(zip(notation, range(0,64)))

m = b.makeMove()[(zipMap["e2"], zipMap["e4"])]
b = b.getCurrentPlayer().makeMove(m)

m = b.makeMove()[(zipMap["e7"], zipMap["e5"])]
b = b.getCurrentPlayer().makeMove(m)

m = b.makeMove()[(zipMap["d2"], zipMap["d4"])]
b = b.getCurrentPlayer().makeMove(m)

m = b.makeMove()[(zipMap["e5"], zipMap["d4"])]
b = b.getCurrentPlayer().makeMove(m)

m = b.makeMove()[(zipMap["e4"], zipMap["e5"])]
b = b.getCurrentPlayer().makeMove(m)

m = b.makeMove()[(zipMap["d4"], zipMap["d3"])]
b = b.getCurrentPlayer().makeMove(m)

m = b.makeMove()[(zipMap["e5"], zipMap["e6"])]
b = b.getCurrentPlayer().makeMove(m)

m = b.makeMove()[(zipMap["d3"], zipMap["c2"])]
b = b.getCurrentPlayer().makeMove(m)

m = b.makeMove()[(zipMap["e6"], zipMap["e7"])]
b = b.getCurrentPlayer().makeMove(m)

while(not b.getCurrentPlayer().isCheckMate()):
    if b.getCurrentPlayer().isCheck():
        print(b.getCurrentPlayer(), "is Checked!")
    
    print(b)
    inputRaw = input('preCord newCord (promoPiece): ')
    data = inputRaw.split()
    try:
        if(len(data) == 2): m = b.makeMove()[(zipMap[data[0]], zipMap[data[1]])]
        elif(len(data) == 3): m = b.makeMove()[(zipMap[data[0]], zipMap[data[1]], data[2])]
        else: m = Move(b, -1, -1, None)
    except:
        m = Move(b, -1, -1, None)
    b = b.getCurrentPlayer().makeMove(m)


