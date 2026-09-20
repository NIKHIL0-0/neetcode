class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        st=deque()
        dic={'(':')','{':'}','[':']'}
        for i in s:
            if i in ['(','{','[']:
                st.append(i)
            else:
                if st and dic[st[-1]]==i:
                    st.pop()
                else:
                    return False
        if len(st)!=0:
            return False
        return True
        