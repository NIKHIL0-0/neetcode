class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]

        def rec(opleft,tot,temp):
            if tot==0 and opleft==0:
                res.append(temp)
                return

            if temp=="" or temp[-1]=='(':
                if opleft>0:
                    rec(opleft-1,tot+1,temp+'(')
                if tot>0:
                    rec(opleft,tot-1,temp+')')
            else:
                if temp=="" or tot>0:
                    rec(opleft,tot-1,temp+')')
                if opleft>0:
                    rec(opleft-1,tot+1,temp+'(')

        rec(n,0,"")
        return res