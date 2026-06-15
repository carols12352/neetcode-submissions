class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = Counter(s1)
        left = 0
        for right in range(len(s2)):
            cnt[s2[right]] -= 1
            while cnt[s2[right]] < 0:
                cnt[s2[left]] += 1
                left += 1
            if right - left + 1 == len(s1):
                return True
        return False
