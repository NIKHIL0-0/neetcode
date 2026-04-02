class Solution:
    def numDecodings(self, s: str) -> int:
        dp=[0]*(len(s)+1)
        dp[0]=1
        dp[1]=0 if s[0]=='0' else 1
        for i in range (2,len(s)+1):
            od=int(s[i-1:i])
            td=int(s[i-2:i])
            if od>=1:
                dp[i]+=dp[i-1]
            if td>=10 and td<=26:
                dp[i]+=dp[i-2]
        return dp[-1]
        