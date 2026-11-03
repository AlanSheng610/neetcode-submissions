class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for i, char in enumerate(s):
            if char in "({[":
                stack.append(char)
            else:
                if not stack:
                    return False

                if stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False