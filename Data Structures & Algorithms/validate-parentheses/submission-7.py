class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        q = deque()
        for i in range(len(s)):
            if self.isopp(s[i]):
                if not q:
                    return False
                if s[i] != self.bracket(q[-1]):
                    return False
                else:
                    q.pop()
            else:  
                q.append(s[i])
        return len(q) == 0


    def bracket(self, bra: str) -> str:
        if bra == '(':
            return ')'
        elif bra == '{':
            return '}'
        else:
            return ']'
    def isopp(self, bra:str) -> bool:
        if bra == ')' or bra == '}' or bra ==']':
            return True
        return False
