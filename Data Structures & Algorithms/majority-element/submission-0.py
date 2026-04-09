class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        maps={}

        thres = len(nums)/2

        for num in nums:
            maps[num] = maps.get(num, 0)+1

            if maps[num]>thres:
                return num

        
        