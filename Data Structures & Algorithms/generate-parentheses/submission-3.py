class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def rec(temp, op, cl, tot):

            if tot < 0:
                return

            if tot == 0 and op+cl==n*2:
                res.append("".join(temp))

            if op < n:
                temp.append("(")
                rec(temp, op + 1, cl, tot + 1)
                temp.pop()

            if cl < n:
                temp.append(")")
                rec(temp, op, cl + 1, tot - 1)
                temp.pop()

        rec([], 0, 0, 0)

        return res