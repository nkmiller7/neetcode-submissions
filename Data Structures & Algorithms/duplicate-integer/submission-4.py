class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueNums = set()
        for n in nums:
            if n in uniqueNums:
                return True
            else: 
                uniqueNums.add(n)
        return False
        