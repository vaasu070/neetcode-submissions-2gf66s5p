class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        # approach 1
        freq={}

        thre = len(nums)//3

        for num in nums:
            freq[num] = freq.get(num, 0)+1
        
        res = []
        for num ,freq in freq.items():
            if freq>thre:
                res.append(num)

        return res


