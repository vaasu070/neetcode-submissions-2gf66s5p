class Solution:
    def decodeString(self, s: str) -> str:
        
        count_stack = []
        str_stack = []
        curr = ''
        k = ''

        for char in s:
            if char.isdigit():
                k = k+char
            elif char =='[':
                count_stack.append(k)
                str_stack.append(curr)
                k = ''
                curr=''
            elif char==']':
                count = int(count_stack.pop())
                temp  =str_stack.pop()
                curr = temp+ count*curr            
            else:
                curr+=char
        return curr
