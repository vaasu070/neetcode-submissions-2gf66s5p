class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()

        l , r = 0 , 0

        max_length = 1

        lenght = 0

        x= False

        if len(s) ==0:
            return 0
        while r<=len(s)-1:

            char = s[r]

           

            if char in seen:
                l+=1
                r =l
                max_length = max(lenght ,max_length )
                seen = set()
                lenght =0
                x = True
            else:
                seen.add(char)
                r+=1
                lenght+=1
                x = False
            print(lenght ,char , l , r ,seen)
        

        if x==False:
           return max(lenght,max_length)

        return max_length


