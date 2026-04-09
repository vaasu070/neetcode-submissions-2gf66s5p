class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:


    


        # approach 1

        # if sum(nums)<target:
        #     return 0
        # res = len(nums)

        # for i in range(0, len(nums)):
        #     total = 0
        #     for j in range(i , len(nums)):
        #         total = total+nums[j]
        #         if total>=target:
        #             print(res,total,  j-i+1)
        #             res  = min(res, j-i+1)
        #             break
        # return res


        #approach 2


        res = float('inf')
        l  =0
        r = 0

        total = 0

        while l<=r and r<len(nums):
            total = total + nums[r]
            print(total)

            while total>=target:
                res = min(res , r-l+1)

                total-=nums[l]
                l+=1

            r+=1
        return 0 if res == float('inf') else res
        










        