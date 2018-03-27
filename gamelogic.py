class Set:
    def findset(self):
        for i in range(0,len(board) - 2):
            c1 = board[i]
            for j in range(i + 1,len(board) - 1):
                c2 = board[j]
                for k in range(j + 1,len(board)):
                    c3 = board[k]
                    if (checkSet(c1, c2, c3)):
                        foundSet = [c1, c2, c3]
                        return foundset

    def checkSet(self,card1,card2,card3):
        if(card1 == None or card2 == None or card3 == None):
            raise ValueError('Wrong Data Type')
        return isAllSameorDiff(card1['color'],card2['color'], card3['color']) and isAllSameorDiff(card1['shape'], card2['shape'], card3['shape']) and isAllSameorDiff(card1['shading'], card2['shading'], card3['shading']) and isAllSameorDiff(card1['number'], card2['number'], card3['number'])

    def isAllSameorDiff(self,a,b,c):
        return (a == b and a == c and b == c) or (a != b and a != c and b != c)

    def removeSet(self,pos1, pos2, pos3):
        board.splice(pos1, 1)
        board.splice(pos2, 1)
        board.splice(pos3, 1)