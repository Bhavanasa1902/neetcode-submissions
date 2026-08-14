class Solution:
    def isValid(self, s: str) -> bool:
       stack = []
       closetoOpen = {")" :"(", "}" : "{", "]":"["}

       for c in s:
        if c not in closetoOpen:
            stack.append(c)
        else:
            if stack and stack[-1] == closetoOpen[c]:
                stack.pop()
            else:
                return False
       return not stack