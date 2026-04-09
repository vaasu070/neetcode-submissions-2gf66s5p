class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix_array =  [0]* len(nums)
        postfix_array = [0]* len(nums)

        prefix_array[0] = nums[0]
        for i  in range(1 ,len(nums)):
            prefix_array[i]  =prefix_array[i-1]*nums[i]
        
        postfix_array[-1] = nums[-1]
        for i  in range(len(nums)-2 ,-1, -1):
            print(i)
            postfix_array[i]  =postfix_array[i+1]*nums[i]
        
        print(prefix_array, postfix_array  )


        res= [0]*len(nums)
        res[0] = postfix_array[1]
        res[-1] = prefix_array[-2]

        for i in range(1, len(nums)-1):
            print(i)
            res[i] = prefix_array[i-1] * postfix_array[i+1]
        

        return res
        print(res)

        

        