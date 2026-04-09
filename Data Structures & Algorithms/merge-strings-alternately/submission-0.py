class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        i,j =0,0

        max_len = max(len(word1), len(word2))

        res =''

        for i in range(0, max_len):
            print(i)
            if i>len(word1)-1:
                res+=word2[i:len(word2)]
                return res
            elif i>len(word2)-1:
                res+=word1[i:len(word1)]
                return res
            else:
        
                res= res+ word1[i] + word2[i]
            print(res)
        return res


    

        