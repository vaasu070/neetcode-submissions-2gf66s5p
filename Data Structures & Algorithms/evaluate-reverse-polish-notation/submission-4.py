class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for ele in tokens:
            
            if ele =='+':
                stack.append(stack.pop()+ stack.pop())
            elif ele=='-':
                a = stack.pop() 
                b = stack.pop()
                stack.append(b-a)
            elif ele=='*':
                a = stack.pop() 
                b = stack.pop()
                stack.append(b*a)
            elif ele=='/':
                a = stack.pop() 
                b = stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(ele))
        return stack[0]



        