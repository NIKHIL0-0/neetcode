class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        from collections import defaultdict
        dic=defaultdict(int)
        if len(wall[0])==1:
            return len(wall)
        for row in wall:
            temp=0
            for i in row:
                if i+temp!=sum(wall[0]):
                    dic[i+temp]+=1
                    temp+=i
        ans= len(wall)-max(dic.values())
        return ans




        