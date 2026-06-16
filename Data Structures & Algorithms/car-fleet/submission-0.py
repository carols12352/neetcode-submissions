class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # time = []
        # maxfleet = len(position)
        
        # for i in range(len(position)):
        #     time.append((target-position[i])/speed[i])
        # cur = 0
        # for i in range(len(time)):
        #     if time[i] <= time[cur]:
        #         maxfleet -= 1
        #         cur += 1
            
        # return maxfleet
        cars = sorted(zip(position, speed))

        times = [(target-i[0])/i[1] for i in cars ]
        fleet = 0
        cur_time = 0

        for t in reversed(times):
            if t > cur_time:
                fleet += 1
                cur_time = t
        return fleet

        





