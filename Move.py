import math

class Move(): 

    def __init__(self, board, fromT, toT, movedP):
        self.__board = board
        self.__fromT = fromT
        self.__toT = toT
        self.__movedP = movedP

    def exec(self):
        newBoard = {}
        for (k, v) in self.__board.getConfig().items():
            if v is self.__movedP:
                newBoard[k] = None
            else:
                newBoard[k] = v

        # En Passant Move
        if (self.__movedP.getType() == 'Pawn'
                and abs(self.__toT - self.__fromT) == 16):
            p = self.__movedP.movePiece(self, True)
            newBoard[self.__toT] = p
        elif self.__movedP.getType() == 'Pawn':
            p = self.__movedP.movePiece(self, False)
            newBoard[self.__toT] = p
        else:
            newBoard[self.__toT] = self.__movedP.movePiece(self)
        
        newBoard[64] = 'White' if self.__board.getConfig()[64] == 'Black' else 'Black'

        return newBoard

    def getPreCord(self):
        return self.__fromT

    def getNewCord(self):
        return self.__toT

    def getMovedPiece(self):
        return self.__movedP

    def getBoard(self):
        return self.__board

    def __repr__(self):
        return f"Move({self.__fromT, self.__movedP, self.__toT})"

    def __hash__(self):
        return hash(self.__fromT + self.__toT + self.__movedP.__hash__())

    def __eq__(self, other):
        return (self.__class__ == other.__class__ 
        and self.__fromT == other.getPreCord()
        and self.__toT == other.getNewCord()
        and self.__movedP == other.getMovedPiece()
        and self.__board == other.getBoard())

class AttackMove(Move):

    def __init__(self, board, fromT, toT, movedP, attackedP):
        super().__init__(board, fromT, toT, movedP)
        self.__attackedP = attackedP

    def exec(self):
        newBoard = {}
        for (k, v) in super().getBoard().getConfig().items():
            if (v is super().getMovedPiece()
                or v is self.__attackedP):
                newBoard[k] = None
            else:
                newBoard[k] = v

        # En Passant Move
        if super().getMovedPiece().getType() == 'Pawn':
            p = super().getMovedPiece().movePiece(self, False)
            newBoard[super().getNewCord()] = p
        else:
            newBoard[super().getNewCord()] = super().getMovedPiece().movePiece(self)
        
        newBoard[64] = 'White' if super().getBoard().getConfig()[64] == 'Black' else 'Black'

        return newBoard
    
    def getAttackedPiece(self):
        return self.__attackedP

    def __repr__(self):
        return f"AttackMove({super().getPreCord(), super().getMovedPiece(), super().getNewCord(), self.__attackedP})"

    def __hash__(self):
        sup = super().__hash__()
        return hash(str(sup) + self.__attackedP.getType())

    def __eq__(self, other):
        return (super().__eq__(self, other) 
        and self.__attackedP == other.getAttackedPiece())

class PromotionMove(Move):

    def __init__(self, board, fromT, toT, movedP, promoteP, attackedP = None):
        super().__init__(board, fromT, toT, movedP)
        self.__promoteP = promoteP
        self.__attackedP = attackedP

    def exec(self):
        newBoard = {}
        for (k, v) in super().getBoard().getConfig().items():
            if (v is super().getMovedPiece()
                or (self.__attackedP is not None 
                    and v is self.__attackedP)):
                newBoard[k] = None
            else:
                newBoard[k] = v

        newBoard[super().getNewCord()] = self.__promoteP
        
        newBoard[64] = 'White' if super().getBoard().getConfig()[64] == 'Black' else 'Black'
        
        return newBoard
    
    def getPromotedPiece(self):
        return self.__promoteP

    def __repr__(self):
        return f"AttackMove({super().getPreCord(), super().getMovedPiece(), super().getNewCord(), self.__promoteP, self.__attackedP})"

    def __hash__(self):
        sup = super().__hash__()
        return hash(str(sup) + self.__promoteP.getType())

    def __eq__(self, other):
        return (super().__eq__(self, other) 
        and self.__promoteP == other.getPromotedPiece())

class CastleMove(Move):

    def __init__(self, board, fromT, toT, movedP, rookP, rookNewCord):
        super().__init__(board, fromT, toT, movedP)
        self.__rookP = rookP
        self.__rookNewCord = rookNewCord

    def exec(self):
        newBoard = {}
        for (k, v) in super().getBoard().getConfig().items():
            if (v is super().getMovedPiece()
                or v is self.__rookP):
                newBoard[k] = None
            else:
                newBoard[k] = v

        newBoard[super().getNewCord()] = super().getMovedPiece().movePiece(self)
        newBoard[self.__rookNewCord] = self.__rookP.movePiece(self)
        
        newBoard[64] = 'White' if super().getBoard().getConfig()[64] == 'Black' else 'Black'

        return newBoard

    def getRookPiece(self):
        return self.__rookP

    def __repr__(self):
        return f"CastleMove({super().getPreCord(), super().getMovedPiece(), super().getNewCord(), self.__rookP})"

    def __hash__(self):
        sup = super().__hash__()
        return hash(str(sup) + str(self.__rookNewCord))

    def __eq__(self, other):
        return (super().__eq__(self, other) 
        and self.__rookP == other.getRookPiece())