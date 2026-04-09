class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # maps={}

        # thres = len(nums)//2

        # for num in nums:
        #     maps[num] = maps.get(num, 0)+1

        #     if maps[num]>thres:
        #         return num


        candidate = nums[0]
        count  =0

        for num in nums:

            if count ==0:
                candidate = num

            if num==candidate:
                count+=1
            else:
                count-=1
            
        return candidate



        
        
        