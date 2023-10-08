class Solution:
    def isvalid(self, s: str) -> bool:
        stack = []
        corresbrackets = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in corresbrackets:
                if stack and stack[-1] == corresbrackets[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
    

solution = Solution()
s = "{[()]}}"
result = solution.isvalid(s)
print(result)

