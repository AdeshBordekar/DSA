class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            curr = max(nums[i], curr + nums[i])
            res = max(res, curr)

        return res