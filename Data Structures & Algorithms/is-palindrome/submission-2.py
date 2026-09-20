# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         def checkpal(st):
#             l=0
#             r=len(st)-1
#             while l<=r:       
#                 if st[l]==st[r]:
#                     l+=1
#                     r-=1
#                 else:
#                     return False
#             return True
#         st=""
#         for i in s:
#             if i.isalnum():
#                 st+=i.lower()
#         return checkpal(st)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True