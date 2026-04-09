class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result ={}

        for i , num in enumerate(nums):
            remaining = target-num

            if remaining not in result:
                result[num]=i
            else:
                x = result[remaining]
                y = i
                return [x, y]
                

        

        

   
            

        