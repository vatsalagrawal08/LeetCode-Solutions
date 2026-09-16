class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        current_sum = 0
        max_sum = 0
        left = 0
        count = {}

        for right in range(len(nums)):
            current_sum += nums[right]
            count[nums[right]] = count.get(nums[right], 0) + 1
            if right - left + 1 > k:
                outgoing = nums[left]

                current_sum -= outgoing
                count[outgoing] -= 1

                if count[outgoing] == 0:
                    del count[outgoing]

                left += 1
            if right - left + 1 == k and len(count) == k:
                max_sum = max(max_sum, current_sum)

        return max_sum

