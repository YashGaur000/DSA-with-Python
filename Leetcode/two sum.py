class Solution:
    def twosum(self, nums, target):
        seen = {}
        for i, value in enumerate(nums):
            remaining = target-nums[i]
            if remaining in seen:
                return [i, seen[remaining]]
            else:
                seen[value] = i
                print(seen)


solution = Solution()
nums = [1, 2, 8, 5, 3, 4, 6]
target = 7
result = solution.twosum(nums, target)
print(result)



