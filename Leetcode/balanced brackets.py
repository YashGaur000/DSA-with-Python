'''Given a string s containing just the characters '(' , ')' , '{' , '}' ,
'[' & ']' , determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.

Open brackets must be closed in the correct order.

Every close bracket has a corresponding open bracket of the same type
'''

class Solution:
    def isvalid(self, s:str)->bool:
        stack=[]
        corresbrackets={")":"(", "}":"{","]":"["}
        for c in s:
            if c in corresbrackets:
                if stack and stack[-1] == corresbrackets[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
    
solution=Solution()
s="{[()]}}"
result=solution.isvalid(s)
print(result)