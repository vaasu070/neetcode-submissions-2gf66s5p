class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix_array, suffix_array= [1]*len(nums),[1]*len(nums)

    
        for i in range(len(nums)):

     

            if i ==0:
                prefix_array[i]= nums[i]
            else:
                prefix_array[i] = prefix_array[i-1] * nums[i] 
          

    

        for i in range(len(nums)-1,-1,-1):
          

            if i ==len(nums)-1:
                suffix_array[i] = nums[i]
            else:
                suffix_array[i] = suffix_array[i+1] * nums[i]
               


        print(prefix_array,suffix_array )


        output  = [1]*len(nums)

        for i , num in enumerate(nums):
            if i ==0:
                 output[i]= suffix_array[1]
            elif i==len(nums)-1:
                output[i]= prefix_array[i-1]
            else:
                output[i]= prefix_array[i-1] * suffix_array[i+1]

        print(output)



        return output
        
        