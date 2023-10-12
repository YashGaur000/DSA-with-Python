class Solution:
    def palindrome(self, strng):
        l, r = 0, len(strng)-1
        while l < r:
            while not self.alnum(strng[l]):
                l += 1
            while not self.alnum(strng[r]):
                r -= 1
            if strng[l].lower() != strng[r].lower():
                return False
            l, r = l+1, r-1
        return True
            
    def alnum(self, s):
        return (ord("A") <= ord(s) <= ord("Z") or
                ord("a") <= ord(s) <= ord("z") or
                ord("0") <= ord(s) <= ord("9"))
    
solution = Solution()
result = solution.palindrome("A man, a plan, a canal: panama")
print(result)
