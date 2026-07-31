class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic={}
        l=0
        maxi=0
        for r in range (len(s)):
            if s[r] not in dic:
                dic[s[r]]=1
                maxi=max(maxi,r-l+1)
            else:
                while s[l]!=s[r] and l<r:
                    del dic[s[l]]
                    l+=1
                if s[l]==s[r] and l<r:
                    l+=1

        return maxi

        

            
        