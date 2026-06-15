class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = Counter()
        max_freq = 0
        left = 0
        ans = 0

        for right in range((len(s))):
            cnt[s[right]] += 1

            max_freq = max(max_freq, cnt[s[right]])

            while right - left + 1 - max_freq > k:
                cnt[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)
        return ans