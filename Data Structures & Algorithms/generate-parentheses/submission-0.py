class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(temp, openbraces, opens_used, tot):
            if tot == 2 * n:
                if openbraces == 0:
                    res.append("".join(temp))
                return

            # Add '('
            if opens_used < n:
                temp.append("(")
                backtrack(temp, openbraces + 1, opens_used + 1, tot + 1)
                temp.pop()

            # Add ')'
            if openbraces > 0:
                temp.append(")")
                backtrack(temp, openbraces - 1, opens_used, tot + 1)
                temp.pop()

        backtrack([], 0, 0, 0)
        return res