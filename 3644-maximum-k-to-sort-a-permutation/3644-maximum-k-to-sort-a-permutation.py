
from typing import List

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)

        if all(nums[i] == i for i in range(n)):
            return 0

        k = -1

        for i in range(n):
            if nums[i] != i:
                k &= nums[i] & i

        return k


        