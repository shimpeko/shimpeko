class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m + n
        while i > 0:
            i = i - 1
            if n == 0:
                continue
            if m == 0:
                nums1[i] = nums2[n - 1]
                n = n -1
                continue
    
            a, b = nums1[m - 1], nums2[n - 1]
            if a >= b:
                nums1[i] = a
                m = m - 1
            else:
                nums1[i] = b
                n = n - 1
