class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        need = Counter(t) 

        left = 0
        right = 0
        window = {}
        valid = 0
        length = 10086
        start = 0


        while right < len(s):
            c = s[right]

            right += 1

            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
  
            while valid == len(need):
                if right - left < length:
                    start = left
                    length = right - left

                d = s[left]
                left += 1

                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1


        return "" if length == 10086 else s[start:start+length]


        