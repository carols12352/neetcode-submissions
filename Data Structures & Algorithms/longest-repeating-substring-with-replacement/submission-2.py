class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxf = 0
        left = right = 0
        res = 0
        while right < len(s):
            count[s[right]] = count.get(s[right], 0) + 1
            maxf = max(maxf, count[s[right]])
            if right - left + 1 - maxf > k:
                count[s[left]] -= 1
                left += 1
            res = max(right - left + 1, res)
            right += 1
        return res
            

