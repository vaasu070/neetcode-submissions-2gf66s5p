class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

        # nums = [ 1, 0 , 0 , 3,0 , 4, 5]

        # [0, 1 , 0, 3, 4, 5]
        # [0, , 0 , 1 , 3, 4, 5]

        k  =0
        for i in range(0 , len(nums)):

            if nums[i]==0:
                nums[k], nums[i] = nums[i], nums[k]
                k+=1
        
        print(nums)

        index_1  = nums.index(1) if 1 in nums else None
        if index_1:
            for i in range(index_1 , len(nums)):
                if nums[i]==1:
                    nums[k], nums[i] = nums[i], nums[k]
                    k+=1
                

        print(nums) 
        index_2  = nums.index(2)  if 2 in nums else None
        if index_2:
            for i in range(index_2 , len(nums)):

                if nums[i]==2:
                    nums[k], nums[i] = nums[i], nums[k]
                    k+=1
            
        return nums
            

