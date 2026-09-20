class Solution:
    def isValidSudoku(self, nums: List[List[str]]) -> bool:
        for i in range (9):
            temp=set()
            for j in range (9):
                if nums[i][j]!=".":
                    if nums[i][j] in temp:
                        return False
                    temp.add(nums[i][j])
        ls=[(0,0),(0,1),(0,2),(1,0),(2,0),(1,2),(1,1),(2,1),(2,2)]
        for r in range (0,7,3):
            for c in range (0,7,3):
                temp=set()
                for rr,cc in ls:
                    i=rr+r
                    j=cc+c
                    if nums[i][j]!='.':
                        if nums[i][j] in temp:
                            return False
                        temp.add(nums[i][j])
        for j in range(9):
            temp = set()
            for i in range(9):
                if nums[i][j] != ".":
                    if nums[i][j] in temp:
                        return False
                    temp.add(nums[i][j])
        return True


        