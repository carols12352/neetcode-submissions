class MinStack:

    def __init__(self):
        self.sta = []        

    def push(self, val: int) -> None:
        self.sta.append(val)
        

    def pop(self) -> None:
        self.sta.pop()
        

    def top(self) -> int:
        return self.sta[-1]
        

    def getMin(self) -> int:
        return min(self.sta)
            
        
