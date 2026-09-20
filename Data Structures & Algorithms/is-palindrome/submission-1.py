class Solution:
    def isPalindrome(self, s: str) -> bool:
        def checkpal(st):
            l=0
            r=len(st)-1
            while l<=r:       
                if st[l]==st[r]:
                    l+=1
                    r-=1
                else:
                    return False
            return True
        st=""
        for i in s:
            if i.isalnum():
                st+=i.lower()
        return checkpal(st)
            