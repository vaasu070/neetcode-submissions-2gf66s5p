class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # approach 1

        prefix = [1]* len(nums)
        postfix = [1]* len(nums)

        prod = 1
        for i in range(len(nums)):
            prod = prod*nums[i]
            prefix[i] = prod

        prod = 1
        for i in range(len(nums)-1,-1, -1):
         
            prod = prod*nums[i]
            postfix[i] = prod

        
        res = [1]* len(nums)

        for i in range(len(nums)):
            if i==0:
                res[i] =1 *  postfix[i+1]
            elif i+1>=len(nums):
                res[i] =prefix[i-1] *  1
            else:
                res[i] =prefix[i-1] *  postfix[i+1]



            

        return res





