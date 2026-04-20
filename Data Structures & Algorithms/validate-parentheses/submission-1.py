class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = "({["
        closes = ")}]"
        brack_lst = ["{}", "[]", "()"]
        pop = lambda: stack.pop() if stack else "EMPTY"
        if len(s) < 2 or all(char in opens for char in s):
            return False
        for char in s:
            if char in opens:
                stack.append(char)
            elif char in closes:
                if len(stack) == 0:
                    return False
                stack_top = stack[-1]
                if stack_top + char in brack_lst:
                    pop()
                else:
                    return False
        return len(stack) == 0