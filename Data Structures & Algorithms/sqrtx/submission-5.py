class Solution:
    def mySqrt(self, x: int) -> int:


        if x ==1:
            return 1
        res = 0
        for i in range(1, x//2+1):
            
            if i*i>x:
                break
            res = i
        return res
            
        