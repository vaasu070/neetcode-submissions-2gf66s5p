class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        hash_map = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,
       'n':14,"o":15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}


        def get_freq(x):

            result = [0]*26
         
           
            for char in x:
                index = hash_map[char]
                result[index] = result[index] +1
            return str(result)


    

        final_result={}

        for i in range(len(strs)):
            st = strs[i]

            freq = get_freq(st)
            

            
            # print(final_result)
            # print( st)
            # print( freq)
            # print('--------')
            if freq in final_result:

                final_result[freq].append(st)
            else:
                final_result[freq] = [st]

        
        return list(final_result.values())

        

 
            



                



            

            

        