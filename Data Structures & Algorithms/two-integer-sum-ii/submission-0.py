class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        seen = {}

        for i,num in enumerate(numbers) :
            rem =target - num 
            print(num, rem , seen)
            if rem in seen:
                return [seen[rem]+1,i+1]
            else:
                seen[num] = i
            



        


        