class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # res = []
        # approach 1
        # for i  in range(len(temperatures)):
        #     diff = 0
        #     for j in range(i , len(temperatures)):
        #         if temperatures[j]>temperatures[i]:
        #             diff = j-i
        #             break
        #     res.append(diff)
        # return res

        res = [0]* len(temperatures)
        stack  =[]
        

        for i  in range(0, len(temperatures)):
            curr_temp = temperatures[i]
            while stack and curr_temp>temperatures[stack[-1]]:       
                res[stack[-1]] = i-stack[-1]
                stack.pop()
            stack.append(i)
        return res



