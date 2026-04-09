class Solution:
    def decodeString(self, s: str) -> str:


        stack = []

        for char in s:
            
            if char!=']':
                stack.append(char)
            else:
                sub_str = ''

                while stack[-1] != '[':
                    sub_str=stack.pop()+ sub_str
                
                stack.pop()
                k=''
                
                while stack and stack[-1].isdigit():
                     k= stack.pop()+k
                
                stack.append(int(k) * sub_str)
        
        
        return ''.join(stack)
                



