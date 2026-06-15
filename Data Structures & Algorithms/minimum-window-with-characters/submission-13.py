class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ''
        left = 0
        cnt = Counter(t)
        need = len(t)
        for right in range(len(s)):
            if cnt[s[right]] > 0:
                need -= 1
            cnt[s[right]] -= 1

            while need == 0:
                if res == '':
                    res = s[left:right + 1]
                elif len(res) > len(s[left:right + 1]):
                    res = s[left:right + 1]
                
                cnt[s[left]] += 1
                if cnt[s[left]] > 0:
                    need += 1
                left += 1
        return res
