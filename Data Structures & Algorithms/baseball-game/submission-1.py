class Solution:
    def calPoints(self, operations: List[str]) -> int:


        res =[]
        for i , op in enumerate(operations) :
           
            if op=='+':

                res.append(int(res[-1]) + int(res[-2]))
            elif op=='C':
                res.pop()
            elif op=='D':
                res.append(2*int(res[-1]))
            else:
                res.append(int(op))
            print(res, op, i)
        return sum(res)
            

            

        