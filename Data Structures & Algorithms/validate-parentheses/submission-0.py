class Solution:
    def isValid(self, s: str) -> bool:
        stk = deque()
        for c in s:
            if not stk:
                stk.append(c)
            elif c == ')':
                if stk[-1] != '(':
                    return False
                stk.pop()
            elif c == '}':
                if stk[-1] != '{':
                    return False
                stk.pop()
            elif c == ']':
                if stk[-1] != '[':
                    return False
                stk.pop() 
            else:
                stk.append(c)
        return not stk
