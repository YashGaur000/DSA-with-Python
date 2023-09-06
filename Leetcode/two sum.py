class Solution:
   def twoSum(self, nums, target):
       seen = {}
       for i, value in enumerate(nums):
           remaining = target - nums[i]
           print(i, value)
           if remaining in seen:
               return [i, seen[remaining]]
            
           seen[value] = i 

solution = Solution()
nums=[3,4,6]
target=9
result=solution.twoSum(nums, target)
print(result)