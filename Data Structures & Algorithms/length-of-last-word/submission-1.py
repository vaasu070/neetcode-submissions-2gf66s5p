class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # print(s.split(' '))
        # last_str = s.split(' ')[-1]
        # return len(last_str)

        for i in range(len(s)-1 ,-1, -1):
            print(s[i],i)
            if s[i]==' ':
                continue
            
            count = 0
            while s[i] != ' ' and i >= 0:
                count+=1
                i-=1
            return count
            
            
            



        