class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        sta = []
        days = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while sta and temperatures[i] > temperatures[sta[-1]]:
                prev = sta.pop()
                days[prev] = i - prev

            sta.append(i)
        return days
