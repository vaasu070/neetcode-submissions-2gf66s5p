class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        res  = 0

        freq = {}

        l=0
        maxf=0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r],0)+1

            maxf = max(freq.values())

            while (r - l + 1) - maxf > k:
                freq[s[l]] -= 1
                l += 1

            res = max( r - l + 1,res)
        return res

