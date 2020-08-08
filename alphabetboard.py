class Solution(object):
    def alphabetBoardPath(self, target):
        board =  ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        dic = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                dic[board[i][j]] = (i,j)
        x,y = 0,0
        res = ''
        for i in target:
            x1,y1 = dic[i]
            #
            if i == 'z':
                v = y - y1
                if v > 0:
                    res += 'L' * v
                else:
                    res += 'R' * (-v)
                v = x - x1
                if v > 0:
                    res += 'U' * v
                else:
                    res += 'D' * (-v)
            else:
                v = x - x1
                if v > 0:
                    res += 'U' * v
                else:
                    res += 'D' * (-v)
                v = y - y1
                if v > 0:
                    res += 'L'*v
                else:
                    res += 'R' * (-v)
            res += '!'
            x,y = x1,y1
        return res
val=Solution()
S1=input()
print(val.alphabetBoardPath(S1))
