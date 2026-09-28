class Solution:
    def checkValidString(self, s: str) -> bool:

        memo = {}

        def rec(curr, total):
            if curr == len(s):
                return total == 0

            if total < 0:
                return False

            if (curr, total) in memo:
                return memo[(curr, total)]

            if s[curr] == '(':
                ans = rec(curr + 1, total + 1)

            elif s[curr] == ')':
                ans = rec(curr + 1, total - 1)

            else:
                ans = (
                    rec(curr + 1, total - 1) or
                    rec(curr + 1, total + 1) or
                    rec(curr + 1, total)
                )

            memo[(curr, total)] = ans
            return ans

        return rec(0, 0)