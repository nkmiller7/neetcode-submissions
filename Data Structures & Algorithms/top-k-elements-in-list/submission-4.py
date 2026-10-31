class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for n in nums:
            if n in dic:
                dic[n] = dic[n] + 1
            else:
                dic[n] = 1
        
        sorted_dic = sorted(dic.items(), key=lambda item: item[1])
        sorted_dic = sorted_dic[-k:]
        res = list()
        for i in range(k):
            res.append(sorted_dic[i][0])
        return res
        