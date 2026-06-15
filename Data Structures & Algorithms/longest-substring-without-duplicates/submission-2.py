class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        isthere = {}
        left = 0
        right = 0
        length = 0
        while right < len(s) :
            if s[right] not in isthere or isthere[s[right]] == 0:
                isthere[s[right]] = 1
                right += 1
            else:
                isthere[s[left]] = 0
                left += 1
            
            length = max(length, right - left)
        return max(length, right - left)


