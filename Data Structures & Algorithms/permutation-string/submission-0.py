class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        def get_freq(string):
            freq = [0]*26

            for char in string:

                freq[ord(char)-ord('a')] = 1+ freq[ord(char)-ord('a')]
            

            return freq


        s1_len = len(s1)

        s1_freq = get_freq(s1)
        print(s2)
        
        for i in range(0, len(s2)-s1_len+1):
           
            sub_str = s2[i:s1_len+i]

            s2_freq = get_freq(sub_str)

            print(i, s1_len,sub_str)

            if s2_freq==s1_freq:
                return True
        return False
            