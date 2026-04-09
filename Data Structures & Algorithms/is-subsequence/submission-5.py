class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        print(len(s))
        if len(s)==0:
            if len(t) == 0:
                return True
            else:
                return True
        k = 0
        for i in range(len(s)):
            char = s[i]
            while k<len(t):
                print(i , k)
                if char == t[k]:
                    if i ==len(s)-1:
                        return True
                    k+=1
                    break
                k+=1
            
        return False 
                 

        