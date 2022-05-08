class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c, i):
            if (i == len(word)):
                return True

            if (r < 0 or c < 0 or 
                r >= ROWS or 
                c >= COLS or
                board[r][c] != word[i] ): 
                return False
            
            #mark path
            curr = board[r][c]
            board[r][c] = '-'
            res = (dfs(r+1, c, i+1) or
                   dfs(r-1, c, i+1) or
                   dfs(r, c+1, i+1) or
                   dfs(r, c-1, i+1))  
                   
            #mark back the original value
            board[r][c] = curr
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
                    

        return False
