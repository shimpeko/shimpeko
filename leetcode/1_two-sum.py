class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        candidates = {}
        for i, v in enumerate(nums):
            j = candidates.get(v)
            if j is not None:
                return [i,j]
            candidates[target - v] = i
