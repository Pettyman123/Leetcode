import numpy as np 
import math 

def maxSubarray(nums: list[int]) -> int:
    # Kadane's Algorithm
    cur_sum = 0
    max_sum = float('-inf')
    n = len(nums)

    for i in range(n):
        cur_sum += nums[i]
        max_sum = max(max_sum, cur_sum)
        if cur_sum <0:
            cur_sum = 0
    
    return max_sum

x = [0,-4,1,2]
print(maxSubarray(x))