class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        min_len=len(strs[0])

        for str in strs:
           min_len = min(len(str), min_len)

        print(min_len, 'len')


        res =''
        
        for i in range(min_len):
            start_char = strs[0][i]
            common=True
            for str in strs:
                if str[i]!=start_char:
                    common = False
                    return res

            if common:
                res+=start_char

        
        return res

     
