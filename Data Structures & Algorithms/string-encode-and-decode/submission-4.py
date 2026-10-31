class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(s[::-1] + "*//*")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        temp = s.split("*//*")
        res = []
        for s in temp:
            res.append(s[::-1])
        return res[0:len(res)-1]
