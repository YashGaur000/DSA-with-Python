class Solution:
    def palindrome(self, strng):
        l, r = 0, len(strng)-1
        while l < r:
            while l < r and not self.alnum(strng[l]):
                l += 1
            while r >= l and not self.alnum(strng[r]):
                r -= 1
            
            if strng[l].lower() != strng[r].lower():
                return False
            l, r = l+1, r-1
            
        return True
            
    def alnum(self, s):
        return 'a' <= s.lower() <= 'z' or '0' <= s <= '9'       
    
solution = Solution()
result = solution.palindrome("\"Sue,\" Tom smiles, \"Selim smote us.\"")
print(result)
