class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        sta = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while sta and t > sta[-1][0]:
                staT, staInd = sta.pop()
                res[staInd] = i - staInd
            sta.append((t,i))
        return res