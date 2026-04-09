class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = []
        # approach 1
        for i  in range(len(temperatures)):
            diff = 0
            for j in range(i , len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    diff = j-i
                    break
            res.append(diff)
        return res