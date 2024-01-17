class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] + nums[j]==target and i!=j:
                    return [i, j]

lst = [2, 3, 4, 15]
example  = Solution()
print(example.twoSum(lst, 6))