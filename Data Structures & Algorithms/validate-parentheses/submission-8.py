class Solution:
    def isValid(self, s: str) -> bool:

        if len(s)==1:
            return False

        map = {')':'(',"}":"{","]":"["}

        stack = []

        for item in s:
            if item in map:
                if stack and stack[-1] == map[item]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item) 

        if len(stack)==0:
            return True
        return False

        