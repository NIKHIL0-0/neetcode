class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        from collections import deque
        res=[0]*len(nums)
        st=deque()
        for idx,i in enumerate(nums):
            if not st:
                st.append(idx)
            elif nums[st[-1]]>=i:
                st.append(idx)
            else:
                while st and nums[st[-1]]<i:
                    idd=st.pop()
                    res[idd]=(idx-idd)
                st.append(idx)
        return res

        