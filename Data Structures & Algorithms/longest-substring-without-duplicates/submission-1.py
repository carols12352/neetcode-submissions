class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        apper = []
        maxlen = 0
        left = 0
        right = 0
        while right < len(s):
            if s[right] in apper:
                maxlen = max(maxlen, len(apper))
                apper = []
                left += 1
                right = left
                
            else:
                apper.append(s[right])
                right += 1

            maxlen = max(maxlen, len(apper))

        return maxlen
                
                
