class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        n = len(nums)
        for i in range(n):
            x = target - nums[i]
            if nums[i] in hash:
                return [hash[nums[i]], i]
            else:
                hash[x] = i  

        