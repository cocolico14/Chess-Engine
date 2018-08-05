from abc import ABC, abstractmethod
from Move import * 

class Piece(ABC):

    def __init__(self, cord, side, pieceType, firstMove = True):
        self.__cord = cord
        self.__side = side
        self.__pieceType = pieceType
        self.__firstMove = firstMove
        super().__init__()
    
    @abstractmethod
    def getPossMoves(self, board):pass
    
    @abstractmethod
    def movePiece(self, move):pass

    def getCord(self):
        return self.__cord

    def getSide(self):
        return self.__side

    def getType(self):
        return self.__pieceType

    def isFirstMove(self):
        return self.__firstMove

    def __repr__(self):
        return f"Piece({self.__cord, self.__pieceType, self.__side})"

    def __hash__(self):
        return hash(str(self.__cord) + str(self.__side) + str(self.__pieceType) + str(self.__firstMove))

    def __eq__(self, other):
        return (self.__class__ == other.__class__ 
        and self.__cord == other.getCord()
        and self.__side == other.getSide()
        and self.__pieceType == other.getType()
        and self.__firstMove == other.isFirstMove())

    def __str__(self):
        return ""

class Rook(Piece):

    deltaMoves = [-8, -1, 1, 8]

    def __init__(self, cord, side, firstMove = True):
        super().__init__(cord, side, 'Rook', firstMove)

    def getPossMoves(self, board):
        possMoves = set()
        
        for delta in Rook.deltaMoves:
            tmpCord = super().getCord()
            
            while 0 <= tmpCord < 64:
                if not Rook.checkExclusion(tmpCord, delta): break
                tmpCord += delta
                if 0 <= tmpCord < 64:
                    if not board.getTile(tmpCord):
                        possMoves.add(Move(board, super().getCord(), tmpCord, self))
                    else:
                        if super().getSide() != board.getTile(tmpCord).getSide():
                            possMoves.add(AttackMove(board, super().getCord(), tmpCord, self, board.getTile(tmpCord)))
                        break
        
        return possMoves
    
    @staticmethod
    def checkExclusion(cord, delta):
        if cord % 8 == 0 and delta == -1:
            return False
        elif cord % 8 == 7 and delta == 1:
            return False
        return True

    def getSide(self):
        return super().getSide()

    def movePiece(self, move):
        return Rook(move.getNewCord(), move.getMovedPiece().getSide(), False)
    
    def __str__(self):
        return "R" if super().getSide()=='White' else "r"

class Bishop(Piece):

    deltaMoves = [-9, -7, 7, 9]
    
    def __init__(self, cord, side, firstMove = True):
        super().__init__(cord, side, 'Bishop', firstMove)
    
    def getPossMoves(self, board):
        possMoves = set()
        
        for delta in Bishop.deltaMoves:
            tmpCord = super().getCord()
            
            while 0 <= tmpCord < 64:
                if not Bishop.checkExclusion(tmpCord, delta): break
                tmpCord += delta
                if 0 <= tmpCord < 64:
                    if not board.getTile(tmpCord):
                        possMoves.add(Move(board, super().getCord(), tmpCord, self))
                    else:
                        if super().getSide() != board.getTile(tmpCord).getSide():
                            possMoves.add(AttackMove(board, super().getCord(), tmpCord, self, board.getTile(tmpCord)))
                        break
                     
        return possMoves

    @staticmethod
    def checkExclusion(cord, delta):
        if cord % 8 == 0 and (delta == -9 or delta == 7):
            return False
        elif cord % 8 == 7 and (delta == 9 or delta == -7):
            return False
        return True
    
    def getSide(self):
        return super().getSide()

    def movePiece(self, move):
        return Bishop(move.getNewCord(), move.getMovedPiece().getSide(), False)
    
    def __str__(self):
        return "B" if super().getSide()=='White' else "b"

class Knight(Piece):

    deltaMoves = [-17, -15, -10, -6, 6, 10, 15, 17]
    
    def __init__(self, cord, side, firstMove = True):
        super().__init__(cord, side, 'Knight', firstMove)
    
    def getPossMoves(self, board):
        possMoves = set()
        
        for delta in Knight.deltaMoves:
            newCord = super().getCord() + delta
            
            if Knight.checkExclusion(super().getCord(), delta):
                if 0 <= newCord < 64:
                    if not board.getTile(newCord):
                        possMoves.add(Move(board, super().getCord(), newCord, self))
                    elif super().getSide() != board.getTile(newCord).getSide():
                        possMoves.add(AttackMove(board, super().getCord(), newCord, self, board.getTile(newCord)))

        return possMoves

    @staticmethod
    def checkExclusion(cord, delta):
        if (cord % 8 == 0 
            and (delta == -17 or delta == -10 or delta == 6 or delta == 15)):
            return False
        elif cord % 8 == 1 and (delta == -10 or delta == 6):
            return False
        elif cord % 8 == 6 and (delta == 10 or delta == -6):
            return False
        elif (cord % 8 == 7 
            and (delta == 17 or delta == 10 or delta == -6 or delta == -15)):
            return False
        return True
    
    def getSide(self):
        return super().getSide()

    def movePiece(self, move):
        return Knight(move.getNewCord(), move.getMovedPiece().getSide(), False)
    
    def __str__(self):
        return "N" if super().getSide()=='White' else "n"

class Queen(Piece):

    deltaMoves = [-9, -8, -7, -1, 1, 7, 8, 9]

    def __init__(self, cord, side, firstMove = True):
        super().__init__(cord, side, 'Queen', firstMove)

    def getPossMoves(self, board):
        possMoves = set()
        
        for delta in Queen.deltaMoves:
            tmpCord = super().getCord()
            
            while 0 <= tmpCord < 64:
                if not Queen.checkExclusion(tmpCord, delta): break
                tmpCord += delta
                if 0 <= tmpCord < 64:
                    if not board.getTile(tmpCord):
                        possMoves.add(Move(board, super().getCord(), tmpCord, self))
                    else:
                        if super().getSide() != board.getTile(tmpCord).getSide():
                            possMoves.add(AttackMove(board, super().getCord(), tmpCord, self, board.getTile(tmpCord)))
                        break
        
        return possMoves

    @staticmethod
    def checkExclusion(cord, delta):
        if cord % 8 == 0 and (delta == -9 or delta == -1 or delta == 7):
            return False
        elif cord % 8 == 7 and (delta == 9 or delta == 1 or delta == -7):
            return False
        return True
    
    def getSide(self):
        return super().getSide()

    def movePiece(self, move):
        return Queen(move.getNewCord(), move.getMovedPiece().getSide(), False)
    
    def __str__(self):
        return "Q" if super().getSide()=='White' else "q"

class King(Piece):

    deltaMoves = [-9, -8, -7, -1, 1, 7, 8, 9] 
    
    def __init__(self, cord, side, firstMove = True):
        super().__init__(cord, side, 'King', firstMove)
    
    def getPossMoves(self, board):
        possMoves = set()
        
        for delta in King.deltaMoves:
            newCord = super().getCord() + delta
            
            if King.checkExclusion(super().getCord(), delta):
                if 0 <= newCord < 64:
                    if not board.getTile(newCord):
                        possMoves.add(Move(board, super().getCord(), newCord, self))
                    elif super().getSide() != board.getTile(newCord).getSide():
                        possMoves.add(AttackMove(board, super().getCord(), newCord, self, board.getTile(newCord)))

        return possMoves

    @staticmethod
    def checkExclusion(cord, delta):
        if (cord % 8 == 0 
            and (delta == -9 and delta == -1 and delta == 7)):
            return False
        elif (cord % 8 == 7 
            and (delta == 9 and delta == 1 and delta == -7)):
            return False
        return True
    
    def getSide(self):
        return super().getSide()

    def movePiece(self, move):
        return King(move.getNewCord(), move.getMovedPiece().getSide(), False)
    
    def __str__(self):
        return "K" if super().getSide()=='White' else "k"

class Pawn(Piece):

    deltaMoves = [7, 8, 9, 16]
    
    def __init__(self, cord, side, enPassant, firstMove = True):
        super().__init__(cord, side, 'Pawn', firstMove)
        self.__enPassant = enPassant
    
    def getPossMoves(self, board):
        possMoves = set()
        
        for delta in Pawn.deltaMoves:
            thisDir = -1 if super().getSide() == 'White' else 1
            newCord = super().getCord() + (delta * thisDir)
            midCord = newCord - (thisDir * 8)
            
            if 0 <= newCord < 64:
                if delta == 8 and not board.getTile(newCord):
                    #Pawn Promo
                    if Pawn.checkPromotion(newCord, super().getSide()):
                        possMoves.add(PromotionMove(board, super().getCord(), newCord, self
                                        ,Queen(newCord, super().getSide(), False)))
                        possMoves.add(PromotionMove(board, super().getCord(), newCord, self
                                        ,Rook(newCord, super().getSide(), False)))
                        possMoves.add(PromotionMove(board, super().getCord(), newCord, self
                                        ,Bishop(newCord, super().getSide(), False)))    
                        possMoves.add(PromotionMove(board, super().getCord(), newCord, self
                                        ,Knight(newCord, super().getSide(), False)))                          
                    else:
                        possMoves.add(Move(board, super().getCord(), newCord, self))
                elif (delta == 16 
                        and not board.getTile(newCord)
                        and Pawn.checkPawnJump(self, board, midCord)):
                    # Pawn Jump
                    possMoves.add(Move(board, super().getCord(), newCord, self))

                elif((delta == 9 or delta == 7)
                        and not board.getTile(newCord)
                        and Pawn.checkExclusion(super().getCord(), delta, super().getSide())
                        and Pawn.checkEnPasant(self, midCord, board)):
                    # Pawn En Passant
                    possMoves.add(AttackMove(board, super().getCord(), newCord, self, board.getTile(midCord)))
                
                elif ((delta == 9 or delta == 7)
                        and board.getTile(newCord)
                        and Pawn.checkExclusion(super().getCord(), delta, super().getSide())
                        and super().getSide() != board.getTile(newCord).getSide()):
                    # Pawn Attack + Promotion
                    if Pawn.checkPromotion(newCord, super().getSide()):
                        possMoves.add(PromotionMove(board, super().getCord(), newCord, self
                                        ,Queen(newCord, super().getSide(), False)
                                        ,board.getTile(newCord)))
                        possMoves.add(PromotionMove(board, super().getCord(), newCord, self
                                        ,Rook(newCord, super().getSide(), False)
                                        ,board.getTile(newCord)))
                        possMoves.add(PromotionMove(board, super().getCord(), newCord, self
                                        ,Bishop(newCord, super().getSide(), False),
                                        board.getTile(newCord)))    
                        possMoves.add(PromotionMove(board, super().getCord(), newCord, self
                                        ,Knight(newCord, super().getSide(), False)
                                        ,board.getTile(newCord)))    
                    else:
                        possMoves.add(AttackMove(board, super().getCord(), newCord, self, board.getTile(newCord)))
                    
        return possMoves
    
    
    @staticmethod
    def isStartingRow(cord, side):
        if side == 'Black' and 8 <= cord < 16: return True
        elif side == 'White' and 48 <= cord < 56: return True
        return False
    
    @staticmethod
    def checkExclusion(cord, delta, side):
        if (cord % 8 == 0 
            and ((delta == 7 and side == 'Black') or
                (delta == 9 and side == 'White') )):
            return False
        elif (cord % 8 == 7 
            and ((delta == 7 and side == 'White') or
                (delta == 9 and side == 'Black') )):
            return False
        return True
    
    @staticmethod
    def checkPromotion(newCord, side):
        return ((newCord < 8 and side == 'White') or
                (newCord >= 56 and side == 'Black'))
    
    @staticmethod
    def checkPawnJump(pawn, board, midCord):
        return (pawn.isFirstMove()
                and Pawn.isStartingRow(pawn.getCord(), pawn.getSide())
                and 0 <= midCord < 64
                and not board.getTile(midCord))
    
    @staticmethod
    def checkEnPasant(piece, enPassantCord, board):
        return ( 0 <= enPassantCord < 64
                and board.getTile(enPassantCord)
                and board.getTile(enPassantCord).getType() == 'Pawn'
                and board.getTile(enPassantCord).isEnPassant()
                and piece.getSide() != board.getTile(enPassantCord).getSide())
    
    def isEnPassant(self):
        return self.__enPassant
    
    def getSide(self):
        return super().getSide()

    def movePiece(self, move, enPassant):
        return Pawn(move.getNewCord(), move.getMovedPiece().getSide(), enPassant, False)
    
    def __str__(self):
        return "P" if super().getSide()=='White' else "p"