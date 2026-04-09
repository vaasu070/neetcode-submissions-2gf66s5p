class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res =0
        for num in nums:
            next_num=num+1
            i=1
            while next_num in nums:
                next_num+=1
                i+=1
            res = max(res, i)
        return res

        
        