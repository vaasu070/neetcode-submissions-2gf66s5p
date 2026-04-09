class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq,t_freq = {},{}

        if len(s)!=len(t):
            return False

        for item in range(len(s)):
            s_freq[s[item]] =  s_freq.get(s[item],0)  +1 
            t_freq[t[item]] =  t_freq.get(t[item],0)  + 1


        return s_freq == t_freq

 
    
        