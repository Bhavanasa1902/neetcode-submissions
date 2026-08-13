class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        see = set()
        for n in nums:
            if n in see:
                return True
            else:
                see.add(n)
        return False