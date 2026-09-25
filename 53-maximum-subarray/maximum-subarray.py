class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        current_sum = 0
        for i in nums:
            current_sum = max(i, current_sum + i)
            max_sum = max(current_sum, max_sum)
        return max_sum
        