class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        sta = []

        for i in tokens:
            if i not in ['+', '-', '*', '/']:
                sta.append(int(i))
            elif i == '+':
                a = sta.pop()
                b = sta.pop()
                sta.append(a+b)
            elif i == '-':
                a = sta.pop()
                b = sta.pop()
                sta.append(b-a)
            elif i == '*':
                a = sta.pop()
                b = sta.pop()
                sta.append(a*b)
            else:
                a = sta.pop()
                b = sta.pop()
                sta.append(int(b/a))
        return sta[-1]

            
        