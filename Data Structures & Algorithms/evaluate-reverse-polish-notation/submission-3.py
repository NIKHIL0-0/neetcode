class Solution:
    def evalRPN(self, nums: List[str]) -> int:
        from collections import deque
        st=deque()
        
        for i in nums:
            if i not in "+-*/":
                st.append(i)
            else:
                b=int(st.pop())
                a=int(st.pop())
                if i== '+':
                    result = a + b
                elif i== '-':
                    result = a - b
                elif i == '*':
                    result = a * b
                elif i == '/':
                    result = int(a / b)
                st.append(result)
        return int(st[-1])
