class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        see = set()
        for i in nums:  #n is index
            if i in see:
                return True
            else:
                see.add(i)
        return False