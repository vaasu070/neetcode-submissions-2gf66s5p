class Solution:
    def isPalindrome(self, s: str) -> bool:
        s  = s.lower()

        string = ''
        for char in s:
            if char.isalnum():
                string =  string+char
        print(string)


        i = 0
        j = len(string)-1

        while i<j:

            if string[i]!=string[j]:
                return False
            i=i+1
            j = j-1

        
        return True
            





        






        