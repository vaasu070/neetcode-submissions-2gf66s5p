class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        
        if len(s)==0:
            return 0
        l = 0
        r = 0

        mp=set()

      
        res =1
        while l<=r and r<len(s):
            
            while s[r] in mp:      
                mp.remove(s[l])
                l+=1
            mp.add(s[r])
            r+=1
            print(mp , l , r )
            res  = max(len(mp), res)
        return res




                
            
        