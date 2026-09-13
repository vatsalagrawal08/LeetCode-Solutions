class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in nums[:]:
            if i== val:
                nums.remove(i)
            else:
                count += 1
        return count
        print(nums)

        