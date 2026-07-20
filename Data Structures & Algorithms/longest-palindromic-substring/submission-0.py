class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxi=1
        for i in range (1,len(s)):
            l=r=i
            if r+1<len(s) and s[l]==s[r+1]:
                    r+=1
            while l>=0 and r<len(s) and s[l]==s[r]:
                
                if l-1>=0 and r+1<len(s) and s[l-1]==s[r+1]:
                    l-=1
                    r+=1
                else:
                    break
            if maxi<(r-l+1):
                maxi=r-l+1
                st=l
                ed=r
        return s[st:ed+1]
            

        