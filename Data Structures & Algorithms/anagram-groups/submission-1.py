class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def get_fre(str):
            freq = [0]*26
            for char in str:
                freq[ord(char)-ord('a')]+=1


            return freq


        hash_map = {}
        for _str in strs:
            freq =  get_fre(_str)
            print(freq, _str)
            freq = str(freq)
      
            if freq in hash_map:
                hash_map[freq].append(_str)
            else:
                hash_map[freq] = [_str]

        return list(hash_map.values())

        

        