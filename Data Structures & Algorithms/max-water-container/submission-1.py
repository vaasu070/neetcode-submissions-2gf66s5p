class Solution:
    def maxArea(self, heights: List[int]) -> int:


        l , r = 0,len(heights)-1

        max_output = 0

        while l<r:

            output =  (r-l)* min(heights[l], heights[r])
            max_output = max(max_output, output)

            if heights[l]> heights[r]:
                r-=1
            else:
                l+=1
        return max_output

        