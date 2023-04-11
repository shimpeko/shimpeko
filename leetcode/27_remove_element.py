class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[i] == val:
                tmp = nums[j]
                nums[j] = val
                nums[i] = tmp
                j = j - 1
            else:
                i = i + 1
        return i
