class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        fleet = 0
        cur_time = 0
        times = [(target-i[0])/i[1] for i in cars]

        for t in reversed(times):
            if t > cur_time:
                cur_time = t
                fleet += 1
        return fleet