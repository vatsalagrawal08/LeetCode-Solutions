class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left_product = 1
        right_product = 1
        answer = [1] * len(nums)
        right = len(nums)-1
        for left in range(len(nums)):
            answer[left] = left_product
            left_product *= nums[left]
        for right in range(len(nums)-1,-1,-1):
            answer[right] *= right_product
            right_product *= nums[right]
        return answer

        