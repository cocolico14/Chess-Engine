from abc import ABC, abstractmethod
from Move import CastleMove
 
class Player(ABC):

    def __init__(self, board, possMoves, oppPossMoves):
        self.__board = board
        self.__possMoves = possMoves
        self.__oppPossMoves = oppPossMoves
        super().__init__()

    @abstractmethod
    def getPieces(self):pass
    
    @abstractmethod
    def getKingCastles(self, possMoves, oppMoves):pass

    @abstractmethod
    def getSide(self):pass
    
    @abstractmethod
    def getOpp(self, possMoves, oppMoves):pass
    
    @abstractmethod
    def getKing(self):pass

    def isCheck(self):
        return bool(self.getAttacksOnTile(self.getKing().getCord(), self.getOppPossMoves()))
    
    def isCheckMate(self):
        return bool(self.isCheck() and not self.hasEscapeMoves())
    
    def isStaleMate(self):
        return bool(not self.isCheck() and not self.hasEscapeMoves())
    
    def getPossMoves(self):
        return self.__possMoves

    def getBoard(self):
        return self.__board

    def getOppPossMoves(self):
        return self.__oppPossMoves
   
    def isPossMove(self, move):
        return move in self.__possMoves 

    def makeMove(self, move):
        
        if not self.isPossMove(move):
            return self.__board

        from Board import Board
        newBoard = Board(move.exec())
        
        attackOnKing = Player.getAttacksOnTile(newBoard.getCurrentPlayer().getOpp().getKing().getCord()
                        , newBoard.getCurrentPlayer().getPossMoves())

        if attackOnKing:
            return self.__board
        
        return newBoard
    
    def hasEscapeMoves(self):
        for move in self.__possMoves:
            moveTransition = self.makeMove(move)
            if (moveTransition is not None
                and not moveTransition.getCurrentPlayer().isCheck()):
                print(move)
                return True
        return False

    @staticmethod
    def getAttacksOnTile(cord, moves):
        return set(filter(lambda x : x.getNewCord() == cord, moves)) 

class WhitePlayer(Player):

    def __init__(self, board, possMoves, oppPossMoves):
        super().__init__(board, possMoves, oppPossMoves)

    def getPieces(self):
        super().getBoard().getWhitePieces()
        
    def getSide(self):
        return 'White'
        
    def getOpp(self):
        return super().getBoard().getBlackPlayer()

    def getKing(self): 
        for piece in super().getBoard().getWhitePieces():
            if piece and piece.getType() == 'King':
                return piece
        return None
        
    def getKingCastles(self, possMoves, oppMoves):
        castles = set()

        if super().getKing().isFirstMove() and not super().isCheck():
            # King Side Castle
            if(not super().getBoard().getTile(61)
                and not super().getBoard().getTile(62)):
                    if(not super().getAttacksOnTile(61, oppMoves)
                        and not super().getAttacksOnTile(62, oppMoves)
                        and super().getBoard().getTile(63)
                        and super().getBoard().getTile(63).getType() == 'Rook'):
                        if(super().getBoard().getTile(63)
                            and super().getBoard().getTile(63).isFirstMove()):
                            castles.add(CastleMove(super().getBoard, super().getKing().getCord()
                                        , 62, super().getKing(), super().getBoard().getTile(63), 61))

            # Queen Side Castle
            if(not super().getBoard().getTile(57)
                and not super().getBoard().getTile(58)
                and not super().getBoard().getTile(59)):
                    if(not super().getAttacksOnTile(57, oppMoves)
                        and not super().getAttacksOnTile(58, oppMoves)
                        and not super().getAttacksOnTile(59, oppMoves)
                        and super().getBoard().getTile(56)
                        and super().getBoard().getTile(56).getType() == 'Rook'):
                            if(super().getBoard().getTile(56)
                                and super().getBoard().getTile(56).isFirstMove()):
                                castles.add(CastleMove(super().getBoard, super().getKing().getCord()
                                        , 58, super().getKing(), super().getBoard().getTile(56), 59))
                        
            return castles

class BlackPlayer(Player):

    def __init__(self, board, possMoves, oppPossMoves):
        super().__init__(board, possMoves, oppPossMoves)

    def getPieces(self):
        super().getBoard().getBlackPieces()
        
    def getSide(self):
        return 'Black'
        
    def getOpp(self):
        return super().getBoard().getWhitePlayer()

    def getKing(self): 
        for piece in super().getBoard().getBlackPieces():
            if piece and piece.getType() == 'King':
                return piece
        return None
        
    def getKingCastles(self, possMoves, oppMoves):
        castles = set()

        if super().getKing().isFirstMove() and not super().isCheck():
            # King Side Castle
            if(not super().getBoard().getTile(5)
                and not super().getBoard().getTile(6)):
                    if(not super().getAttacksOnTile(5, oppMoves)
                        and not super().getAttacksOnTile(6, oppMoves)
                        and super().getBoard().getTile(7)
                        and super().getBoard().getTile(7).getType() == 'Rook'):
                        if(super().getBoard().getTile(7)
                            and super().getBoard().getTile(7).isFirstMove()):
                            castles.add(CastleMove(super().getBoard, super().getKing().getCord()
                                        , 6, super().getKing(), super().getBoard().getTile(7), 5))

            # Queen Side Castle
            if(not super().getBoard().getTile(1)
                and not super().getBoard().getTile(2)
                and not super().getBoard().getTile(3)):
                    if(not super().getAttacksOnTile(1, oppMoves)
                        and not super().getAttacksOnTile(2, oppMoves)
                        and not super().getAttacksOnTile(3, oppMoves)
                        and super().getBoard().getTile(0)
                        and super().getBoard().getTile(0).getType() == 'Rook'):
                            if(super().getBoard().getTile(0)
                                and super().getBoard().getTile(0).isFirstMove()):
                                castles.add(CastleMove(super().getBoard, super().getKing().getCord()
                                        , 2, super().getKing(), super().getBoard().getTile(0), 3))
                        
            return castles