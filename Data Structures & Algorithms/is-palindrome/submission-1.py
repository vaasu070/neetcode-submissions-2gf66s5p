class Solution:
    def isPalindrome(self, s: str) -> bool:

        def clean(s):
            res =""
            s = s.lower()
            for char in s:
                if (ord(char)<=ord('z') and ord(char)>=ord('a')) or (ord(char)<=ord('9') and ord(char)>=ord('0')):
                    res+=char
            return res

        

        s = clean(s)
        print(s)
        i = 0
        j = len(s)-1

        while i<j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        
        return True



                    


        