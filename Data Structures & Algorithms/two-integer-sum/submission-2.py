class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        see = {}  # val -> index

        for i, n in enumerate(nums):
            see[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in see and see[diff] != i:
                return [i, see[diff]]
        return []
        