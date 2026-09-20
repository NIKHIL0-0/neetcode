class Solution:
    def evalRPN(self, nums: List[str]) -> int:

        st = []

        for i in nums:

            if i not in "+-*/":
                st.append(int(i))

            else:
                b = st.pop()
                a = st.pop()

                if i == '+':
                    result = a + b
                elif i == '-':
                    result = a - b
                elif i == '*':
                    result = a * b
                else:
                    result = int(a / b)

                st.append(result)

        return st[-1]