class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        dic = {}
        maxi = 0
        res = 0

        for r in range(len(s)):
            dic[s[r]] = dic.get(s[r], 0) + 1
            maxi = max(maxi, dic[s[r]])

            while (r - l + 1) - maxi > k:
                dic[s[l]] -= 1
                if dic[s[l]] == 0:
                    del dic[s[l]]
                l += 1

            res = max(res, r - l + 1)

        return res