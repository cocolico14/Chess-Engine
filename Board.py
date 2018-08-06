from Piece import *
from Player import WhitePlayer, BlackPlayer
from Move import PromotionMove
 
class Board():

    def __init__(self, config):
        self.__config = config
        self.__turn = config[64]
        self.__whitePieces = []
        self.__blackPieces = []

        for v in range(0,64):
            if config[v]:
                if config[v].getSide() == 'White':
                    self.__whitePieces.append(config[v])
                else:
                    self.__blackPieces.append(config[v])

        self.__whitePossMoves = Board.getAllPossMoves(self.__whitePieces, self)
        self.__blackPossMoves = Board.getAllPossMoves(self.__blackPieces, self)

        self.__whitePlayer = WhitePlayer(self, self.__whitePossMoves, self.__blackPossMoves)
        self.__blackPlayer = BlackPlayer(self, self.__blackPossMoves, self.__whitePossMoves)

        self.__currentPlayer = self.__whitePlayer if self.__turn == 'White' else self.__blackPlayer

    @staticmethod
    def getAllPossMoves(pieces, board):
        allPossMoves = set()
        
        for p in pieces:
            allPossMoves.update(p.getPossMoves(board))

        return allPossMoves
    
    @staticmethod
    def initializeBoard():
        conf = {}
        for i in range(0,64):
            conf[i] = None

        conf[0] = Rook(0, 'Black')
        conf[1] = Knight(1, 'Black')
        conf[2] = Bishop(2, 'Black')
        conf[3] = Queen(3, 'Black')
        conf[4] = King(4, 'Black')
        conf[5] = Bishop(5, 'Black')
        conf[6] = Knight(6, 'Black')
        conf[7] = Rook(7, 'Black')
        conf[8] = Pawn(8, 'Black', False)
        conf[9] = Pawn(9, 'Black', False)
        conf[10] = Pawn(10, 'Black', False)
        conf[11] = Pawn(11, 'Black', False)
        conf[12] = Pawn(12, 'Black', False)
        conf[13] = Pawn(13, 'Black', False)
        conf[14] = Pawn(14, 'Black', False)
        conf[15] = Pawn(15, 'Black', False)

        conf[48] = Pawn(48, 'White', False)
        conf[49] = Pawn(49, 'White', False)
        conf[50] = Pawn(50, 'White', False)
        conf[51] = Pawn(51, 'White', False)
        conf[52] = Pawn(52, 'White', False)
        conf[53] = Pawn(53, 'White', False)
        conf[54] = Pawn(54, 'White', False)
        conf[55] = Pawn(55, 'White', False)
        conf[56] = Rook(56, 'White')
        conf[57] = Knight(57, 'White')
        conf[58] = Bishop(58, 'White')
        conf[59] = Queen(59, 'White')
        conf[60] = King(60, 'White')
        conf[61] = Bishop(61, 'White')
        conf[62] = Knight(62, 'White')
        conf[63] = Rook(63, 'White')

        conf[64] = 'White'

        return conf

    def makeMove(self):
        test = {}
        for move in self.__blackPossMoves.union(self.__whitePossMoves):
            if type(move) is PromotionMove : 
                test[(move.getPreCord(), move.getNewCord(), str(move.getPromotedPiece()) )] = move
            else:
                test[(move.getPreCord(), move.getNewCord())] = move
        
        return test

    def getTile(self, cord):
        return self.__config[cord]

    def getConfig(self):
        return self.__config

    def getWhitePieces(self):
        return self.__whitePieces

    def getBlackPieces(self):
        return self.__blackPieces

    def getWhitePlayer(self):
        return self.__whitePlayer

    def getBlackPlayer(self):
        return self.__blackPlayer

    def getCurrentPlayer(self):
        return self.__currentPlayer

    def getTurn(self):
        return self.__turn

    def __repr__(self):
        return f"Board()"

    def __eq__(self, other):
        return (self.__class__ == other.__class__ 
        and self.__config == other.getConfig())

    def __str__(self):
        res = ""
        for i in range(0, 8):
            res += str(8 - i) + " "
            for j in range(0, 8):
                if self.__config[i*8 + j] != None:
                    res += str(self.__config[i*8 + j]) + " "
                else:
                    res += "-" + " "
            res += "\n"
        res += "  a b c d e f g h"
        return res
    
    