from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window=len(s1)
        dic1=Counter(s1)
        dic2=Counter(s2[:window])
        l=0
        for r in range (window,len(s2)):
            if dic1.items()==dic2.items():
                return True
            else:
                dic2[s2[l]]-=1
                if dic2[s2[l]]==0:
                    del dic2[s2[l]]
                l+=1
                dic2[s2[r]]=dic2.get(s2[r],0)+1
        return dic1 == dic2
                
