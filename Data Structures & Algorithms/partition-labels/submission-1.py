class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        def mergi(dic):
            res=[]
            prev=-1
            ls=sorted(dic.values())
            last=ls[0][1]
            for st,ed in ls[1:]:
                if st<=last:
                    last=max(last,ed)
                else:
                    res.append(last-prev)
                    prev=last
                    last=ed
            res.append(last - prev )
            return res
        from collections import defaultdict
        dic=defaultdict(list)
        
        for idx,i in enumerate(s):
            if not dic[i]:
                dic[i].append(idx)
                dic[i].append(idx)
            else:
                dic[i][1]=idx
        
        return mergi(dic)
                    







        