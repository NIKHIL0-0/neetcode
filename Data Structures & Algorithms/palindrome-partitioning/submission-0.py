class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def ispal(st):
            l = 0
            r = len(st)-1

            while l <= r:
                if st[l] != st[r]:
                    return False
                l += 1
                r -= 1

            return True

        res = []

        def rec(temp, st):

            if st == len(s)-1:
                res.append(temp[:])
                return

            for i in range(st+1, len(s)):
                part = s[st+1:i+1]

                if ispal(part):
                    temp.append(part)
                    rec(temp, i)
                    temp.pop()

        rec([], -1)
        return res