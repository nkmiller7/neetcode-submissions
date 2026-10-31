class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numSet = set(nums)

        for n in numSet:
            if (n - 1) not in numSet:
                leng = 1 
                while (n + leng) in numSet:
                    leng += 1
                res = max(leng, res)
        
        return res