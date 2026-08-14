class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     see = {} # hash set -> index

     for i, n in enumerate(nums):
        see[n] = i
     for i, n in enumerate(nums):
        complement = target - n
        if complement in see and see[complement] != i:
            return [i, see[complement]]


        