class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        max_idx = len(height) - 1
        current_r_idx = max_idx            
        for l_idx, l_height in enumerate(height):
            # if l_idx and r_idx will getting closer for each iteration
            # exit the loop when they meet
            if l_idx == current_r_idx:
                break
            # Iterate from rightend
            # current_r_idx starts from max_idx and decrease to zero
            for r_idx in range(current_r_idx, 0, -1):
                r_height = height[r_idx]
                current_area = min(l_height, r_height) * (r_idx - l_idx)
                if current_area > max_area:
                    max_area = current_area
                # When most right bar is at least as high as the current left bar
                # it means the bar provide max area for the current left bar
                # so we can jump to next left bar
                if r_height >= l_height:
                    break
                # Otherwise, keep the the left bar at current idx and 
                # move the right bar towards left by one
                current_r_idx = r_idx
                # This means idx (right or left) with higher bar stays
                # the existing position and indx with lower bar moves
                # Example
                # [1,2,3,2,1]
                #  ^       ^ = 4
                # [1,2,3,2,1]
                #    ^     ^ = 3    
                # [1,2,3,2,1]
                #    ^   ^   = 4
                # [1,2,3,2,1]
                #      ^ ^   = 4
                # [1,2,3,2,1]
                #      ^     = 0
                # end loop
        return max_area
