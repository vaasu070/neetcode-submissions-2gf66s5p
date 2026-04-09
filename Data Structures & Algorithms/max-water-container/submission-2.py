class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        # apporach 1

        res =0

        for i in range(0 , len(heights)):
            for j in range(i+1 , len(heights)):

                min_height = min(heights[i], heights[j])
                

                vol = min_height*(j-i)
                print(min_height, i , j, vol)
                res = max(vol, res)
        print(res)
        return res



