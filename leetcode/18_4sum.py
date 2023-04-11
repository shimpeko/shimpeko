class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        nums_length = len(nums)
        answer = []
        prev_num_1 = None
        # two loops to choose two numbers in a list
        for i, num_1 in enumerate(nums):
            # pathetic effort to exit loop earlier
            if prev_num_1 == num_1:
                continue
            prev_num_1 = num_1
            prev_num_2 = None
            for j, num_2 in enumerate(nums[i+1:]):
                # another pathetic effort to exit loop earlier
                if prev_num_2 == num_2:
                    continue
                prev_num_2 = num_2
                l_idx = i + 1 + j + 1
                r_idx = nums_length - 1
                while l_idx < r_idx:
                    l_num = nums[l_idx]
                    r_num = nums[r_idx]
                    tmp_sum = num_1 + num_2 + l_num + r_num
                    if tmp_sum == target:
                        candidate = [num_1, num_2, l_num, r_num]
                        if not (candidate in answer):
                            answer.append([num_1, num_2, l_num, r_num])
                        # Which pointer should I move?
                        l_idx = l_idx + 1
                        r_idx = r_idx - 1
                    elif tmp_sum < target:
                        l_idx = l_idx + 1  
                    else:
                        r_idx = r_idx - 1
        return answer

