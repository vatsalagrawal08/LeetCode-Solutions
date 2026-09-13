class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set()
        count =0
        for i in nums:
            if i in s:
                continue
            else:
                s.add(i)
                nums[count] = i
                count += 1
        return count
        