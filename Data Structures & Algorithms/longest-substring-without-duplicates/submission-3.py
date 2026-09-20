class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic={}
        l=0
        maxi=0
        for r in range (len(s)):
            if s[r] not in dic or dic[s[r]]<l:
                dic[s[r]]=r
                maxi=max(maxi,r-l+1)
            else:
                l=dic[s[r]]+1
                dic[s[r]]=r
        return maxi

        

            
        