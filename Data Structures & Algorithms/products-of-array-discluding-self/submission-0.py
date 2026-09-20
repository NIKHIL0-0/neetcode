class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fr=[]
        bc=[]
        temp=1
        for i in nums:
            fr.append(temp)
            temp*=i
        temp=1
        for idx,i in enumerate(nums[::-1]):
            cr=len(nums)-1-idx
            fr[cr]*=temp
            temp*=i

        return fr
            

        