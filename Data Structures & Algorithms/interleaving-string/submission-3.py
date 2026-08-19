class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        memo={}
        def rec(i,j,k):
            if k==len(s3):
                return True
            if (i,j) in memo:
                return memo[(i,j)]
            ans=False
            if i<len(s1) and s1[i]==s3[k]:
                ans=rec(i+1,j,k+1)
            if j<len(s2) and s2[j]==s3[k] and not ans:
                ans=rec(i,j+1,k+1)
            memo[(i,j)]=ans
            return ans
        return rec(0,0,0)
        # return memo[(len(s1)-1,len(s2)-1)]
            
        