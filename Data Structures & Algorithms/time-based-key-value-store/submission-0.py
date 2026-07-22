class TimeMap:
    from collections import defaultdict

    def __init__(self):
        self.data=defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append([timestamp,value])

        

    def get(self, key: str, timestamp: int) -> str:
        prev=""
        for time,val in self.data[key]:
            if time==timestamp:
                return val
            elif time>timestamp:
                return prev
            else:
                prev=val
        return prev
        
