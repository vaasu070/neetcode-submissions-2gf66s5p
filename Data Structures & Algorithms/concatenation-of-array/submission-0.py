class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums
        for i in range(0, len(nums)):
            print(i)
            ans.append(nums[i])

        return ans

            
        