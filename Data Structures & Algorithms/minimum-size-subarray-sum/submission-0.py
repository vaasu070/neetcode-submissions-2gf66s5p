class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:


        # res = 0
        # l  =0
        # r = 0

        # while l<r and r<len(nums):


        # approach 1

        if sum(nums)<target:
            return 0
        res = len(nums)

        for i in range(0, len(nums)):
            
            total = 0
            for j in range(i , len(nums)):
                total = total+nums[j]
                if total>=target:
                    print(res,total,  j-i+1)
                    res  = min(res, j-i+1)
                    break
        return res





        