class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        def get_freq(nums):
            freq = {}
            for num in nums:
                freq[num] = freq.get(num, 0)+1

            return freq


        res =[[]]
        for _ in nums:
            res.append([])

        # print(res)


        num_freq = get_freq(nums)


        for num , freq  in num_freq.items():

            res[freq].append(num)

        print(res)
      

        final_res = []
        
        for i in range(len(res)-1, -1, -1):

            
        
            if len(res[i])!=0:
                final_res.extend(res[i])
              
                if len(final_res)==k:
                    return final_res

            print(i , len(res[i]), final_res,k , count)

        
        return final_res









        