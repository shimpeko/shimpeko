class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        nums_length = len(nums)
        answer = None
        for idx, num in enumerate(nums):
            # p is left idx
            p = idx + 1
            # j is right idx
            j = nums_length -1
            # loop while p meets j
            while(p < j):
                tmp_sum = num + nums[p] + nums[j]
                # abs(a-b) = distance between a and b
                if (answer is None) or (abs(target - tmp_sum) <= abs(target - answer)):
                    answer = tmp_sum
                if target > tmp_sum:
                    p = p + 1
                elif target < tmp_sum:
                    j = j - 1
                else:
                    return answer
        return answer
