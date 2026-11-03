class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxi = max(nums)
        moves = 0

        for num in nums:
            moves += maxi - num

        return moves
        