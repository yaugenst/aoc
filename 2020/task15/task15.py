#!/usr/bin/env python3

spoken = {}
nums = [17, 1, 3, 16, 19, 0]
for idx in range(2020):  # 30000000
    if idx < len(nums):
        n = nums[idx]
    elif spoken[n][0] is None:
        n = 0
    else:
        n = spoken[n][1] - spoken[n][0]
    spoken[n] = (None, idx) if n not in spoken else (spoken[n][1], idx)

print(n)
