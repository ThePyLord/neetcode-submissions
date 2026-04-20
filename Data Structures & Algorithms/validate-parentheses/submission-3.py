class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = list(')}]')
        matches = {
            ']': '[',
            ')': '(',
            '}': '{'
        }
        for par in s:
            if par in matches:
                if stack and stack[-1] == matches[par]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(par)
        return len(stack) == 0