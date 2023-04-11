class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) -1 
        i = 0

        def swap(x, y):
            nums[x], nums[y] = nums[y], nums[x]

        while i <= r:
            if nums[i] == 0:
                swap(i,l)
                l = l + 1
                i = i + 1
            elif nums[i] == 2:
                swap(i,r)
                r = r - 1
            else:
                i = i + 1
