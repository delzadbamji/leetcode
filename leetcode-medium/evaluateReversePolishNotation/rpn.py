# import math
class Solution:
    def evaluate(self,a,b,token):
        if token=="+":
            return a+b
        elif token=="-":
            return a-b
        elif token=="*":
            return a*b
        else:
            # if b<0 and a>0:
                # temp = int(a/abs(b))
                # return temp*-1 
            # else:
                return int(a/b)
        
        
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        
        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))
            else:
                b=stack.pop()
                a=stack.pop()
                stack.append(self.evaluate(a,b,i))
        return stack.pop()
