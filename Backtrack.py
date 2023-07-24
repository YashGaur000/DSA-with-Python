#Finding the number of permutation of a given array

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        if len(nums) == 1:
            return [nums.copy()]
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)

            result.extend(perms)
            nums.append(n)

        return result


# Example usage
solution = Solution()
nums = [1, 2, 3]
output = solution.permute(nums)
print(output)
