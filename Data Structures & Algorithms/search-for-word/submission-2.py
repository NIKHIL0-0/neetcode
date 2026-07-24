class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r=len(board)
        c=len(board[0])
        def backtrack(i,j,k):
            if k==len(word):
                return True
            if not (0<=i<r and 0<=j<c) or word[k]!=board[i][j] or board[i][j]=='#':
                return False
            q=board[i][j]
            board[i][j]='#'
            found=(backtrack(i,j+1,k+1) or
                backtrack(i+1,j,k+1) or
                backtrack(i-1,j,k+1) or
                backtrack(i,j-1,k+1))
            board[i][j]=q
            return found

        for i in range (len(board)):
            for j in range (len(board[0])):
                if board[i][j]==word[0]:
                    res=backtrack(i,j,0)
                    if res:
                        return True
        return False
        