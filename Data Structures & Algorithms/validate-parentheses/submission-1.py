class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        sta = []
        left = 0

        while left < len(s):
            if s[left] in [')', '}', ']']:
                if not sta or sta[-1] != self.helper(s[left]):
                    return False
                sta.pop()

            else:
                sta.append(s[left])

            left += 1

        return len(sta) == 0

    def helper(self, s: str) -> str:
        if s == ')':
            return '('
        elif s == '}':
            return '{'
        elif s == ']':
            return '['