class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        _s = []
        _t =[]

        if len(s)!=len(t):
            return False

        for item in s:
            _s.append(item)
        
        for item in t:
            _t.append(item)

        _s.sort()
        _t.sort()
        for x in range(len(_s)):
            if _s[x] != _t[x]:
                return False

        return True

        