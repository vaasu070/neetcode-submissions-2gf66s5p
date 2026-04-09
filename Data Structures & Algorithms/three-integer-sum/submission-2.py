class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res =[]

        for i , num in enumerate(nums):
            a = num
            # ignore if the next ele is same as previous ele
            if i>0 and a==nums[i-1]:
                continue
         

            l = i+1
            r= len(nums)-1
            while l<r:
                tar  = a + nums[l] + nums[r]
            

                # 

                if tar>0:
                    r-=1
                elif tar<0:
                    l+=1
                else:
                    res.append([a , nums[l], nums[r]])
                    l+=1
                    r-=1

                    while nums[l]==nums[l-1] and l<r:
                        l+=1

        print(res)

        return res
        




        