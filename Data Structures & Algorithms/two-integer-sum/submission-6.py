class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            curr = nums[i]
            if target-curr in dic:
                return [dic.get(target-curr), i]
            else: 
                dic[curr] = i
        return [0,0]


        