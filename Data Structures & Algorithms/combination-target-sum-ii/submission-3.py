class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(temp, st, total):
            if total == target:
                res.append(temp[:])
                return

            if total > target:
                return

            for i in range(st, len(candidates)):
                if i > st and candidates[i] == candidates[i - 1]:
                    continue

                temp.append(candidates[i])
                backtrack(temp, i + 1, total + candidates[i])
                temp.pop()

        backtrack([], 0, 0)
        return res