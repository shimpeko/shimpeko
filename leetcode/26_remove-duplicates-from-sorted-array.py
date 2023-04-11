class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        prev_n = None
        while idx < len(nums):
            n = nums[idx]
            if n == prev_n:
                nums.pop(idx)
                continue
            prev_n = n
            idx = idx + 1
        return idx