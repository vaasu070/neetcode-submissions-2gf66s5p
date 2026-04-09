class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = False
        for num in nums:
            if nums.count(num)>1:
                result = True
                break
        return result

 

