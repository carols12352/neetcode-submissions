class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        sta = []
        pointer = 0
        while pointer < len(tokens):
            if tokens[pointer] in ['+','*','/','-']:
                if tokens[pointer] == '+':
                    sta.append(int(sta.pop(-2)) + int(sta.pop()))
                elif tokens[pointer] == '-':
                    sta.append(int(sta.pop(-2)) - int(sta.pop()))
                elif tokens[pointer] == '*':
                    sta.append(int(sta.pop(-2)) * int(sta.pop()))
                else:
                    sta.append(int(sta.pop(-2)) / int(sta.pop()))
            else:
                sta.append(int(tokens[pointer]))
            pointer+=1
        return int(sta.pop())