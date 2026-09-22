class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        dtc = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        def rec(i,temp):
            if len(temp)==len(digits):
                res.append(temp)
                return
            for c in dtc[digits[i]]:
                rec(i+1,temp+c)
        if digits:
            rec(0,"")
        return res 
        