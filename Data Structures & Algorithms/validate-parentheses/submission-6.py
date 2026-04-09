class Solution:
    def isValid(self, s: str) -> bool:

        if len(s)==1:
            return False

        map = {')':'(',"}":"{","]":"["}

        stack = []

        for item in s:
            if stack and item in map and stack[-1] == map[item]:
                stack.pop()
            else:
                stack.append(item) 

        if len(stack)==0:
            return True
        return False

        