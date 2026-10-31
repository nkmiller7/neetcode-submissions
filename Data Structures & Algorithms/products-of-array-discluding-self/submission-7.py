class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product, zero_cnt = 1, 0
        
        containsZero = 0
        for n in nums:
            if n != 0:
                product *= n 
            else:
                zero_cnt += 1
        
        if zero_cnt > 1:
            return [0] * len(nums)

        res = []
        for n in nums:
            if zero_cnt:
                if n:
                    res.append(0)
                else:
                    res.append(product)
            else:
                res.append(product // n)
                
        return res
            
        